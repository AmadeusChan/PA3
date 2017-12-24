package decaf.translate;

import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import decaf.tree.Tree;
import decaf.backend.OffsetCounter;
import decaf.error.RuntimeError;
import decaf.machdesc.Intrinsic;
import decaf.scope.ClassScope;
import decaf.symbol.Class;
import decaf.symbol.Function;
import decaf.symbol.Symbol;
import decaf.symbol.Variable;
import decaf.tac.Functy;
import decaf.tac.Label;
import decaf.tac.Tac;
import decaf.tac.Temp;
import decaf.tac.VTable;
import decaf.type.BaseType;
import decaf.type.Type;

import decaf.tac.*;
import decaf.type.*;

public class Translater {
	private List<VTable> vtables;

	private List<Functy> funcs;

	private Functy currentFuncty;

	public Translater() {
		vtables = new ArrayList<VTable>();
		funcs = new ArrayList<Functy>();
	}

	public Functy getCurrentFuncty() {
		return currentFuncty;
	}

	public static Translater translate(Tree.TopLevel tree) {
		Translater tr = new Translater();
		TransPass1 tp1 = new TransPass1(tr);
		tp1.visitTopLevel(tree);
		TransPass2 tp2 = new TransPass2(tr);
		tp2.visitTopLevel(tree);
		return tr;
	}

	public void printTo(PrintWriter pw) {
		for (VTable vt : vtables) {
			pw.println("VTABLE(" + vt.name + ") {");
			if (vt.parent != null) {
				pw.println("    " + vt.parent.name);
			} else {
				pw.println("    <empty>");
			}
			pw.println("    " + vt.className);
			for (Label l : vt.entries) {
				pw.println("    " + l.name + ";");
			}
			pw.println("}");
			pw.println();
		}
		for (Functy ft : funcs) {
			pw.println("FUNCTION(" + ft.label.name + ") {");
			pw.println(ft.paramMemo);
			Tac tac = ft.head;
			while (tac != null) {
				if (tac.opc == Tac.Kind.MARK) {
					pw.println(tac);
				} else {
					pw.println("    " + tac);
				}
				tac = tac.next;
			}
			pw.println("}");
			pw.println();
		}
	}

	public List<VTable> getVtables() {
		return vtables;
	}

	public List<Functy> getFuncs() {
		return funcs;
	}

	public void createFuncty(Function func) {
		Functy functy = new Functy();
		if (func.isMain()) {
			functy.label = Label.createLabel("main", true);
		} else {
			functy.label = Label.createLabel("_"
					+ ((ClassScope) func.getScope()).getOwner().getName() + "."
					+ func.getName(), true);
		}
		functy.sym = func;
		func.setFuncty(functy);
	}

	public void beginFunc(Function func) {
		currentFuncty = func.getFuncty();
		currentFuncty.paramMemo = memoOf(func);
		genMark(func.getFuncty().label);
	}

	public void endFunc() {
		funcs.add(currentFuncty);
		currentFuncty = null;
	}

	private Tac memoOf(Function func) {
		StringBuilder sb = new StringBuilder();
		Iterator<Symbol> iter = func.getAssociatedScope().iterator();
		while (iter.hasNext()) {
			Variable v = (Variable) iter.next();
			Temp t = v.getTemp();
			if (t instanceof ComplexTemp) {
				t.offset = v.getOffset();
				sb.append(((ComplexTemp) t).re.name + ":" + t.offset + " ");
				sb.append(((ComplexTemp) t).im.name + ":" + (t.offset + 4) + " ");
			} else {
				t.offset = v.getOffset();
				sb.append(t.name + ":" + t.offset + " ");
			}
		}
		if (sb.length() > 0) {
			return Tac.genMemo(sb.substring(0, sb.length() - 1));
		} else {
			return Tac.genMemo("");
		}
	}

	public void createVTable(Class c) {
		if (c.getVtable() != null) {
			return;
		}
		VTable vtable = new VTable();
		vtable.className = c.getName();
		vtable.name = "_" + c.getName();
		vtable.entries = new Label[c.getNumNonStaticFunc()];
		fillVTableEntries(vtable, c.getAssociatedScope());
		c.setVtable(vtable);
		vtables.add(vtable);
	}

	private void fillVTableEntries(VTable vt, ClassScope cs) {
		if (cs.getParentScope() != null) {
			fillVTableEntries(vt, cs.getParentScope());
		}

		Iterator<Symbol> iter = cs.iterator();
		while (iter.hasNext()) {
			Symbol sym = iter.next();
			if (sym.isFunction() && !((Function) sym).isStatik()) {
				Function func = (Function) sym;
				vt.entries[func.getOrder()] = func.getFuncty().label;
			}
		}
	}

	public void append(Tac tac) {
		if (currentFuncty.head == null) {
			currentFuncty.head = currentFuncty.tail = tac;
		} else {
			tac.prev = currentFuncty.tail;
			currentFuncty.tail.next = tac;
			currentFuncty.tail = tac;
		}
	}

	public Temp genAdd(Temp src1, Temp src2) {
		if ((src1 instanceof ComplexTemp) || (src2 instanceof ComplexTemp)) {
			if (!(src1 instanceof ComplexTemp)) {
				src1 = genInt2Comp(src1);
			}
			if (!(src2 instanceof ComplexTemp)) {
				src2 = genInt2Comp(src2);
			}
			return genCompAdd((ComplexTemp) src1, (ComplexTemp) src2);
		}
		Temp dst = Temp.createTempI4();
		append(Tac.genAdd(dst, src1, src2));
		return dst;
	}

	public Temp genSub(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genSub(dst, src1, src2));
		return dst;
	}

	public Temp genMul(Temp src1, Temp src2) {
		if ((src1 instanceof ComplexTemp) || (src2 instanceof ComplexTemp)) {
			if (!(src1 instanceof ComplexTemp)) {
				src1 = genInt2Comp(src1);
			}
			if (!(src2 instanceof ComplexTemp)) {
				src2 = genInt2Comp(src2);
			}
			return genCompMul((ComplexTemp) src1, (ComplexTemp) src2);
		}
		Temp dst = Temp.createTempI4();
		append(Tac.genMul(dst, src1, src2));
		return dst;
	}

	public Temp genDiv(Temp src1, Temp src2) {
		genCheckDivisor(src2);
		Temp dst = Temp.createTempI4();
		append(Tac.genDiv(dst, src1, src2));
		return dst;
	}

	public Temp genMod(Temp src1, Temp src2) {
		genCheckDivisor(src2);
		Temp dst = Temp.createTempI4();
		append(Tac.genMod(dst, src1, src2));
		return dst;
	}

	public void genCheckDivisor(Temp divisor) {
		Label exit = Label.createLabel();
		genBnez(divisor, exit);
		Temp msg = genLoadStrConst(RuntimeError.DIVIDED_BY_ZERO);
		genParm(msg);
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		genIntrinsicCall(Intrinsic.HALT);
		genMark(exit);
	}

	public Temp genNeg(Temp src) {
		Temp dst = Temp.createTempI4();
		append(Tac.genNeg(dst, src));
		return dst;
	}

	public Temp genLAnd(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genLAnd(dst, src1, src2));
		return dst;
	}

	public Temp genLOr(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genLOr(dst, src1, src2));
		return dst;
	}

	public Temp genLNot(Temp src) {
		Temp dst = Temp.createTempI4();
		append(Tac.genLNot(dst, src));
		return dst;
	}

	public Temp genGtr(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genGtr(dst, src1, src2));
		return dst;
	}

	public Temp genGeq(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genGeq(dst, src1, src2));
		return dst;
	}

	public Temp genEqu(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genEqu(dst, src1, src2));
		return dst;
	}

	public Temp genNeq(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genNeq(dst, src1, src2));
		return dst;
	}

	public Temp genLeq(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genLeq(dst, src1, src2));
		return dst;
	}

	public Temp genLes(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genLes(dst, src1, src2));
		return dst;
	}

	public void genAssign(Temp dst, Temp src) {
		//System.out.println("*******log*****: " + (dst instanceof ComplexTemp) + " " + (src instanceof ComplexTemp));
		if (src instanceof ComplexTemp) {
			//return ;
			append(Tac.genAssign(((ComplexTemp) dst).re, ((ComplexTemp) src).re));
			append(Tac.genAssign(((ComplexTemp) dst).im, ((ComplexTemp) src).im));
		} else {
			append(Tac.genAssign(dst, src));
		}
	}

	public Temp genLoadVTable(VTable vtbl) {
		Temp dst = Temp.createTempI4();
		append(Tac.genLoadVtbl(dst, vtbl));
		return dst;
	}

	public Temp genIndirectCall(Temp func, Type retType) {
		if (retType.equal(BaseType.COMPLEX)) {
			Temp add = Temp.createTempI4();
			append(Tac.genIndirectCall(add, func));
			return genLoad(add, 0, true);
		}
		Temp dst;
		if (retType.equal(BaseType.VOID)) {
			dst = null;
		} else {
			dst = Temp.createTempI4();
		}
		append(Tac.genIndirectCall(dst, func));
		return dst;
	}

	public Temp genDirectCall(Label func, Type retType) {
		if (retType.equal(BaseType.COMPLEX)) {
			Temp add = Temp.createTempI4();
			append(Tac.genDirectCall(add, func));
			return genLoad(add, 0, true);
		}
		Temp dst;
		if (retType.equal(BaseType.VOID)) {
			dst = null;
		} else {
			dst = Temp.createTempI4();
		}
		append(Tac.genDirectCall(dst, func));
		return dst;
	}

	public Temp genIntrinsicCall(Intrinsic intrn) {
		if (intrn.type.equal(BaseType.COMPLEX)) {
			Temp add = Temp.createTempI4();
			append(Tac.genDirectCall(add, intrn.label));
			return genLoad(add, 0, true);
		}
		Temp dst;
		if (intrn.type.equal(BaseType.VOID)) {
			dst = null;
		} else {
			dst = Temp.createTempI4();
		}
		append(Tac.genDirectCall(dst, intrn.label));
		return dst;
	}

	// what about the return type is complex? 
	public void genReturn(Temp src) {
		if (src instanceof ComplexTemp) {
			genParm(genLoadImm4(8));
			Temp add = genIntrinsicCall(Intrinsic.ALLOCATE);
			genStore(src, add, 0);
			append(Tac.genReturn(add));
		} else {
			append(Tac.genReturn(src));
		}
	}

	public void genBranch(Label dst) {
		append(Tac.genBranch(dst));
	}

	public void genBeqz(Temp cond, Label dst) {
		append(Tac.genBeqz(cond, dst));
	}

	public void genBnez(Temp cond, Label dst) {
		append(Tac.genBnez(cond, dst));
	}

	public Temp genLoad(Temp base, int offset, boolean isComplex) {
		if (isComplex) {
			ComplexTemp dst = new ComplexTemp();
			append(Tac.genLoad(dst.re, base, Temp.createConstTemp(offset)));
			append(Tac.genLoad(dst.im, base, Temp.createConstTemp(offset + 4)));
			return (Temp) dst;
		} else {
			Temp dst = Temp.createTempI4();
			append(Tac.genLoad(dst, base, Temp.createConstTemp(offset)));
			return dst;
		}
	}

	/*
	public Temp genLoadComp(Temp base, int offset) {
		ComplexTemp dst = new ComplexTemp();
		append(Tac.genLoad(dst.re, base, Temp.createConstTemp(offset)));
		append(Tac.genLoad(dst.im, base, Temp.createConstTemp(offset + 4)));
		return dst;
	}
	*/

	public void genStore(Temp src, Temp base, int offset) {
		if (src instanceof ComplexTemp) {
			append(Tac.genStore(((ComplexTemp) src).re, base, Temp.createConstTemp(offset)));
			append(Tac.genStore(((ComplexTemp) src).im, base, Temp.createConstTemp(offset + 4)));
		} else {
			append(Tac.genStore(src, base, Temp.createConstTemp(offset)));
		}
	}

	public Temp genLoadImm4(int imm) {
		Temp dst = Temp.createTempI4();
		append(Tac.genLoadImm4(dst, Temp.createConstTemp(imm)));
		return dst;
	}

	public Temp genLoadStrConst(String value) {
		Temp dst = Temp.createTempI4();
		append(Tac.genLoadStrConst(dst, value));
		return dst;
	}

	public void genMemo(String comment) {
		append(Tac.genMemo(comment));
	}

	public void genMark(Label label) {
		append(Tac.genMark(label));
	}

	public void genParm(Temp parm) {
		if (parm instanceof ComplexTemp) {
			append(Tac.genParm(((ComplexTemp) parm).re));
			append(Tac.genParm(((ComplexTemp) parm).im));
		} else {
			append(Tac.genParm(parm));
		}
	}

	public void genCheckArrayIndex(Temp array, Temp index) {
		Temp length = genLoad(array, -OffsetCounter.WORD_SIZE, false);
		Temp cond = genLes(index, length);
		Label err = Label.createLabel();
		genBeqz(cond, err);
		cond = genLes(index, genLoadImm4(0));
		Label exit = Label.createLabel();
		genBeqz(cond, exit);
		genMark(err);
		Temp msg = genLoadStrConst(RuntimeError.ARRAY_INDEX_OUT_OF_BOUND);
		genParm(msg);
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		genIntrinsicCall(Intrinsic.HALT);
		genMark(exit);
	}

	public void genCheckNewArraySize(Temp size) {
		Label exit = Label.createLabel();
		Temp cond = genLes(size, genLoadImm4(0));
		genBeqz(cond, exit);
		Temp msg = genLoadStrConst(RuntimeError.NEGATIVE_ARR_SIZE);
		genParm(msg);
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		genIntrinsicCall(Intrinsic.HALT);
		genMark(exit);
	}

	public Temp genNewArray(Temp length, boolean isComplex) {
		genCheckNewArraySize(length);

		if (!isComplex) {
			Temp unit = genLoadImm4(OffsetCounter.WORD_SIZE);
			Temp size = genAdd(unit, genMul(unit, length));
			genParm(size);
			Temp obj = genIntrinsicCall(Intrinsic.ALLOCATE);
			genStore(length, obj, 0);
			Label loop = Label.createLabel();
			Label exit = Label.createLabel();
			Temp zero = genLoadImm4(0);
			append(Tac.genAdd(obj, obj, size));
			genMark(loop);
			append(Tac.genSub(size, size, unit));
			genBeqz(size, exit);
			append(Tac.genSub(obj, obj, unit));
			genStore(zero, obj, 0);
			genBranch(loop);
			genMark(exit);
			return obj;
		} else {
			Temp unit = genLoadImm4(OffsetCounter.COMPLEX_SIZE);
			Temp word = genLoadImm4(OffsetCounter.WORD_SIZE);
			Temp size = genAdd(word, genMul(unit, length));
			genParm(size);
			Temp obj = genIntrinsicCall(Intrinsic.ALLOCATE);
			genStore(length, obj, 0);
			Label loop = Label.createLabel();
			Label exit = Label.createLabel();
			Temp zero = genLoadImm4(0);
			append(Tac.genAdd(obj, obj, size));
			genMark(loop);
			append(Tac.genSub(size, size, word));
			genBeqz(size, exit);
			append(Tac.genSub(obj, obj, word));
			genStore(zero, obj, 0);
			genBranch(loop);
			genMark(exit);
			return obj;
		}
	}

	// should be modified
	public void genNewForClass(Class c) {
		currentFuncty = new Functy();
		currentFuncty.label = Label.createLabel(
				"_" + c.getName() + "_" + "New", true);
		c.setNewFuncLabel(currentFuncty.label);
		currentFuncty.paramMemo = Tac.genMemo("");
		genMark(currentFuncty.label);
		Temp size = genLoadImm4(c.getSize());
		genParm(size);
		Temp newObj = genIntrinsicCall(Intrinsic.ALLOCATE);
		int time = c.getSize() / OffsetCounter.WORD_SIZE - 1;
		if (time != 0) {
			Temp zero = genLoadImm4(0);
			if (time < 5) {
				for (int i = 0; i < time; i++) {
					genStore(zero, newObj, OffsetCounter.WORD_SIZE * (i + 1));
				}
			} else {
				Temp unit = genLoadImm4(OffsetCounter.WORD_SIZE);
				Label loop = Label.createLabel();
				Label exit = Label.createLabel();
				newObj = genAdd(newObj, size);
				genMark(loop);
				genAssign(newObj, genSub(newObj, unit));
				genAssign(size, genSub(size, unit));
				genBeqz(size, exit);
				genStore(zero, newObj, 0);
				genBranch(loop);
				genMark(exit);
			}
		}
		genStore(genLoadVTable(c.getVtable()), newObj, 0);
		genReturn(newObj);
		endFunc();
	}

	public Temp genInstanceof(Temp instance, Class c) {
		Temp dst = Temp.createTempI4();
		Label loop = Label.createLabel();
		Label exit = Label.createLabel();
		Temp targetVp = genLoadVTable(c.getVtable());
		Temp vp = genLoad(instance, 0, false);
		genMark(loop);
		append(Tac.genEqu(dst, targetVp, vp));
		genBnez(dst, exit);
		append(Tac.genLoad(vp, vp, Temp.createConstTemp(0)));
		genBnez(vp, loop);
		append(Tac.genLoadImm4(dst, Temp.createConstTemp(0)));
		genMark(exit);
		return dst;
	}

	public void genClassCast(Temp val, Class c) {
		Label loop = Label.createLabel();
		Label exit = Label.createLabel();
		Temp cond = Temp.createTempI4();
		Temp targetVp = genLoadVTable(c.getVtable());
		Temp vp = genLoad(val, 0, false);
		genMark(loop);
		append(Tac.genEqu(cond, targetVp, vp));
		genBnez(cond, exit);
		append(Tac.genLoad(vp, vp, Temp.createConstTemp(0)));
		genBnez(vp, loop);
		Temp msg = genLoadStrConst(RuntimeError.CLASS_CAST_ERROR1);
		genParm(msg);
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		Temp instanceClassName = genLoad(genLoad(val, 0, false), 4, false);
		genParm(instanceClassName);
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		msg = genLoadStrConst(RuntimeError.CLASS_CAST_ERROR2);
		genParm(msg);
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		Temp targetClassName = genLoad(genLoadVTable(c.getVtable()), 4, false);
		genParm(targetClassName);
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		msg = genLoadStrConst(RuntimeError.CLASS_CAST_ERROR3);
		genParm(msg);
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		genIntrinsicCall(Intrinsic.HALT);
		genMark(exit);
	}

	/*
	public Temp genAdd(Temp src1, Temp src2) {
		Temp dst = Temp.createTempI4();
		append(Tac.genAdd(dst, src1, src2));
		return dst;
	}
	*/

	public ComplexTemp genCompAdd(ComplexTemp src1, ComplexTemp src2) {
		ComplexTemp dst = new ComplexTemp();
		append(Tac.genAdd(dst.re, src1.re, src2.re));
		append(Tac.genAdd(dst.im, src1.im, src2.im));
		return dst;
	}

	public ComplexTemp genCompMul(ComplexTemp src1, ComplexTemp src2) {
		ComplexTemp dst = new ComplexTemp();
		Temp tmp = Temp.createTempI4();
		append(Tac.genMul(dst.re, src1.re, src2.re));
		append(Tac.genMul(tmp, src1.im, src2.im));
		append(Tac.genSub(dst.re, dst.re, tmp));
		append(Tac.genMul(dst.im, src1.re, src2.im));
		append(Tac.genMul(tmp, src1.im, src2.re));
		append(Tac.genAdd(dst.im, dst.im, tmp));
		return dst;
	}

	public ComplexTemp genInt2Comp(Temp src) {
		ComplexTemp dst = new ComplexTemp();
		append(Tac.genAssign(dst.re, src));
		append(Tac.genLoadImm4(dst.im, Temp.createConstTemp(0)));
		return dst;
	}

	public ComplexTemp genLoadCompImg(int img) {
		ComplexTemp dst = new ComplexTemp();
		append(Tac.genLoadImm4(dst.re, Temp.createConstTemp(0)));
		append(Tac.genLoadImm4(dst.im, Temp.createConstTemp(img)));
		return dst;
	}

	public Temp genCompRe(ComplexTemp src) {
		Temp dst = Temp.createTempI4();
		append(Tac.genAssign(dst, src.re));
		return dst;
	}

	public Temp genCompIm(ComplexTemp src) {
		Temp dst = Temp.createTempI4();
		append(Tac.genAssign(dst, src.im));
		return dst;
	}

	public void genPrintComp(ComplexTemp src) {
		genParm(src.re);
		genIntrinsicCall(Intrinsic.PRINT_INT);
		genParm(genLoadStrConst("+"));
		genIntrinsicCall(Intrinsic.PRINT_STRING);
		genParm(src.im);
		genIntrinsicCall(Intrinsic.PRINT_INT);
		genParm(genLoadStrConst("j"));
		genIntrinsicCall(Intrinsic.PRINT_STRING);
	}

	public Temp genSCopy(Tree.Expr expr) {
		Class c = ((ClassType) expr.type).getSymbol();
		Temp obj = genDirectCall(c.getNewFuncLabel(), BaseType.INT);

		Label loop = Label.createLabel();
		Label exit = Label.createLabel();
		Temp cnt = genLoadImm4(c.getSize());
		Temp unit = genLoadImm4(OffsetCounter.WORD_SIZE);

		genMark(loop);
		genBeqz(cnt, exit);
		genAssign(cnt, genSub(cnt, unit));
		genStore(genLoad(genAdd(expr.val, cnt), 0, false), genAdd(obj, cnt), 0);
		genBranch(loop);
		genMark(exit);

		// store vtable
		Temp vt = genLoadVTable(c.getVtable());
		genStore(vt, obj, 0);
		return obj;
	}

	public Temp genDCopy(Temp old_obj, Class c) {
		Temp new_obj = genDirectCall(c.getNewFuncLabel(), BaseType.INT);   

		//Label loop = Label.createLabel();
		//Label exit = Label.createLabel();
		///Temp cnt = genLoadImm4(c.getSize());
		//System.out.println(c.getSize());
		Temp unit = genLoadImm4(OffsetCounter.WORD_SIZE);
		Temp doubleUnit = genLoadImm4(OffsetCounter.COMPLEX_SIZE);

		Temp old_pt = Temp.createTempI4();
		Temp new_pt = Temp.createTempI4();
		genAssign(old_pt, genAdd(old_obj, unit));
		genAssign(new_pt, genAdd(new_obj, unit));

		Iterator<Symbol> iter = c.getAssociatedScope().iterator();
		while (iter.hasNext()) {
			Symbol sym = iter.next();
			if (sym.isVariable()) {
				//System.out.println(sym.getName());
				Variable var = (Variable) sym;
				if (var.getType().isClassType()) {
					//System.out.println("Class");
					genStore(genDCopy(genLoad(old_pt, 0, false), ((ClassType) var.getType()).getSymbol()), new_pt, 0);
					genAssign(old_pt, genAdd(old_pt, unit));
					genAssign(new_pt, genAdd(new_pt, unit));
				} else {
					if (var.getType().equal(BaseType.COMPLEX)) {
						//System.out.println("Complex");
						genStore(genLoad(old_pt, 0, true), new_pt, 0);
						genAssign(old_pt, genAdd(old_pt, doubleUnit));
						genAssign(new_pt, genAdd(new_pt, doubleUnit));
					} else {
						//System.out.println("others");
						genStore(genLoad(old_pt, 0, false), new_pt, 0);
						genAssign(old_pt, genAdd(old_pt, unit));
						genAssign(new_pt, genAdd(new_pt, unit));
					}
				}
			}
		}

		// store vtable
		Temp vt = genLoadVTable(c.getVtable());
		genStore(vt, new_obj, 0);
		return new_obj;
	}

	/*
	// should be modified
	public void genNewForClass(Class c) {
		currentFuncty = new Functy();
		currentFuncty.label = Label.createLabel(
				"_" + c.getName() + "_" + "New", true);
		c.setNewFuncLabel(currentFuncty.label);
		currentFuncty.paramMemo = Tac.genMemo("");
		genMark(currentFuncty.label);
		Temp size = genLoadImm4(c.getSize());
		genParm(size);
		Temp newObj = genIntrinsicCall(Intrinsic.ALLOCATE);
		int time = c.getSize() / OffsetCounter.WORD_SIZE - 1;
		if (time != 0) {
			Temp zero = genLoadImm4(0);
			if (time < 5) {
				for (int i = 0; i < time; i++) {
					genStore(zero, newObj, OffsetCounter.WORD_SIZE * (i + 1));
				}
			} else {
				Temp unit = genLoadImm4(OffsetCounter.WORD_SIZE);
				Label loop = Label.createLabel();
				Label exit = Label.createLabel();
				newObj = genAdd(newObj, size);
				genMark(loop);
				genAssign(newObj, genSub(newObj, unit));
				genAssign(size, genSub(size, unit));
				genBeqz(size, exit);
				genStore(zero, newObj, 0);
				genBranch(loop);
				genMark(exit);
			}
		}
		genStore(genLoadVTable(c.getVtable()), newObj, 0);
		genReturn(newObj);
		endFunc();
	}
	*/

}
