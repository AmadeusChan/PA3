package decaf.translate;

import java.util.Stack;

import decaf.tree.Tree;
import decaf.backend.OffsetCounter;
import decaf.machdesc.Intrinsic;
import decaf.symbol.Variable;
import decaf.tac.Label;
import decaf.tac.Temp;
import decaf.type.BaseType;

import decaf.tac.*;
import decaf.type.*;

public class TransPass2 extends Tree.Visitor {

	private Translater tr;

	private Temp currentThis;
	private Temp currentSuper;

	private Stack<Label> loopExits;

	public TransPass2(Translater tr) {
		this.tr = tr;
		loopExits = new Stack<Label>();
	}

	@Override
	public void visitClassDef(Tree.ClassDef classDef) {
		for (Tree f : classDef.fields) {
			f.accept(this);
		}
	}

	@Override
	public void visitMethodDef(Tree.MethodDef funcDefn) {
		if (!funcDefn.statik) {
			currentThis = ((Variable) funcDefn.symbol.getAssociatedScope()
					.lookup("this")).getTemp();
			//currentSuper = funcDefn.symbol.getAssociatedScope()
		}
		tr.beginFunc(funcDefn.symbol);
		funcDefn.body.accept(this);
		tr.endFunc();
		currentThis = null;
	}

	@Override
	public void visitTopLevel(Tree.TopLevel program) {
		for (Tree.ClassDef cd : program.classes) {
			cd.accept(this);
		}
	}

	@Override
	public void visitVarDef(Tree.VarDef varDef) {
		if (varDef.symbol.isLocalVar()) {
			if (!varDef.symbol.getType().equal(BaseType.COMPLEX)) {
				Temp t = Temp.createTempI4();
				t.sym = varDef.symbol;
				varDef.symbol.setTemp(t);
			} else {
				ComplexTemp t = new ComplexTemp();
				t.sym = varDef.symbol;
				varDef.symbol.setTemp(t);
			}
		}
	}

	@Override
	public void visitBinary(Tree.Binary expr) {
		expr.left.accept(this);
		expr.right.accept(this);
		switch (expr.tag) {
		case Tree.PLUS:
			expr.val = tr.genAdd(expr.left.val, expr.right.val);
			break;
		case Tree.MINUS:
			expr.val = tr.genSub(expr.left.val, expr.right.val);
			break;
		case Tree.MUL:
			expr.val = tr.genMul(expr.left.val, expr.right.val);
			break;
		case Tree.DIV:
			expr.val = tr.genDiv(expr.left.val, expr.right.val);
			break;
		case Tree.MOD:
			expr.val = tr.genMod(expr.left.val, expr.right.val);
			break;
		case Tree.AND:
			expr.val = tr.genLAnd(expr.left.val, expr.right.val);
			break;
		case Tree.OR:
			expr.val = tr.genLOr(expr.left.val, expr.right.val);
			break;
		case Tree.LT:
			expr.val = tr.genLes(expr.left.val, expr.right.val);
			break;
		case Tree.LE:
			expr.val = tr.genLeq(expr.left.val, expr.right.val);
			break;
		case Tree.GT:
			expr.val = tr.genGtr(expr.left.val, expr.right.val);
			break;
		case Tree.GE:
			expr.val = tr.genGeq(expr.left.val, expr.right.val);
			break;
		case Tree.EQ:
		case Tree.NE:
			genEquNeq(expr);
			break;
		}
	}

	private void genEquNeq(Tree.Binary expr) {
		if (expr.left.type.equal(BaseType.STRING)
				|| expr.right.type.equal(BaseType.STRING)) {
			tr.genParm(expr.left.val);
			tr.genParm(expr.right.val);
			expr.val = tr.genDirectCall(Intrinsic.STRING_EQUAL.label,
					BaseType.BOOL);
			if(expr.tag == Tree.NE){
				expr.val = tr.genLNot(expr.val);
			}
		} else {
			if(expr.tag == Tree.EQ)
				expr.val = tr.genEqu(expr.left.val, expr.right.val);
			else
				expr.val = tr.genNeq(expr.left.val, expr.right.val);
		}
	}

	@Override
	public void visitAssign(Tree.Assign assign) {
		assign.left.accept(this);
		assign.expr.accept(this);
		switch (assign.left.lvKind) {
		case ARRAY_ELEMENT:
			Tree.Indexed arrayRef = (Tree.Indexed) assign.left;
			Temp esz;
			if (arrayRef.type.equal(BaseType.COMPLEX)) {
				esz = tr.genLoadImm4(OffsetCounter.COMPLEX_SIZE);
			} else {
				esz = tr.genLoadImm4(OffsetCounter.WORD_SIZE);
			}
			Temp t = tr.genMul(arrayRef.index.val, esz);
			Temp base = tr.genAdd(arrayRef.array.val, t);
			tr.genStore(assign.expr.val, base, 0);
			break;
		case MEMBER_VAR:
			Tree.Ident varRef = (Tree.Ident) assign.left;
			tr.genStore(assign.expr.val, varRef.owner.val, varRef.symbol
					.getOffset());
			break;
		case PARAM_VAR:
		case LOCAL_VAR:
			tr.genAssign(((Tree.Ident) assign.left).symbol.getTemp(),
					assign.expr.val);
			break;
		}
	}

	@Override
	public void visitLiteral(Tree.Literal literal) {
		switch (literal.typeTag) {
		case Tree.INT:
			literal.val = tr.genLoadImm4(((Integer)literal.value).intValue());
			break;
		case Tree.BOOL:
			literal.val = tr.genLoadImm4((Boolean)(literal.value) ? 1 : 0);
			break;
		case Tree.COMPIMG:
			literal.val = tr.genLoadCompImg(((Integer)literal.value).intValue()); 
			break;
		default:
			literal.val = tr.genLoadStrConst((String)literal.value);
		}
	}

	@Override
	public void visitExec(Tree.Exec exec) {
		exec.expr.accept(this);
	}

	@Override
	public void visitUnary(Tree.Unary expr) {
		expr.expr.accept(this);
		switch (expr.tag){
		case Tree.NEG:
			expr.val = tr.genNeg(expr.expr.val);
			break;
		case Tree.GETCOMPRE:
			expr.val = tr.genCompRe((ComplexTemp) expr.expr.val);
			break;
		case Tree.GETCOMPIM:
			expr.val = tr.genCompIm((ComplexTemp) expr.expr.val);
			break;
		case Tree.INT2COMP:
			expr.val = tr.genInt2Comp(expr.expr.val);
			break;
		default:
			expr.val = tr.genLNot(expr.expr.val);
		}
	}

	@Override
	public void visitNull(Tree.Null nullExpr) {
		nullExpr.val = tr.genLoadImm4(0);
	}

	@Override
	public void visitBlock(Tree.Block block) {
		for (Tree s : block.block) {
			s.accept(this);
		}
	}

	@Override
	public void visitThisExpr(Tree.ThisExpr thisExpr) {
		thisExpr.val = currentThis;
	}

	@Override
	public void visitReadIntExpr(Tree.ReadIntExpr readIntExpr) {
		readIntExpr.val = tr.genIntrinsicCall(Intrinsic.READ_INT);
	}

	@Override
	public void visitReadLineExpr(Tree.ReadLineExpr readStringExpr) {
		readStringExpr.val = tr.genIntrinsicCall(Intrinsic.READ_LINE);
	}

	@Override
	public void visitReturn(Tree.Return returnStmt) {
		if (returnStmt.expr != null) {
			returnStmt.expr.accept(this);
			tr.genReturn(returnStmt.expr.val);
		} else {
			tr.genReturn(null);
		}

	}

	@Override
	public void visitPrint(Tree.Print printStmt) {
		for (Tree.Expr r : printStmt.exprs) {
			r.accept(this);
			tr.genParm(r.val);
			if (r.type.equal(BaseType.BOOL)) {
				tr.genIntrinsicCall(Intrinsic.PRINT_BOOL);
			} else if (r.type.equal(BaseType.INT)) {
				tr.genIntrinsicCall(Intrinsic.PRINT_INT);
			} else if (r.type.equal(BaseType.STRING)) {
				tr.genIntrinsicCall(Intrinsic.PRINT_STRING);
			}
		}
	}

	@Override
	public void visitIndexed(Tree.Indexed indexed) {
		indexed.array.accept(this);
		indexed.index.accept(this);
		tr.genCheckArrayIndex(indexed.array.val, indexed.index.val);
		
		Temp esz;
		if (indexed.type.equal(BaseType.COMPLEX)) {
			esz = tr.genLoadImm4(OffsetCounter.COMPLEX_SIZE);
		} else {
			esz = tr.genLoadImm4(OffsetCounter.WORD_SIZE);
		}
		Temp t = tr.genMul(indexed.index.val, esz);
		Temp base = tr.genAdd(indexed.array.val, t);
		indexed.val = tr.genLoad(base, 0, indexed.type.equal(BaseType.COMPLEX));
	}

	@Override
	public void visitIdent(Tree.Ident ident) {
		if(ident.lvKind == Tree.LValue.Kind.MEMBER_VAR){
			ident.owner.accept(this);
		}
		
		switch (ident.lvKind) {
		case MEMBER_VAR:
			ident.val = tr.genLoad(ident.owner.val, ident.symbol.getOffset(), ident.symbol.getType().equal(BaseType.COMPLEX));
			break;
		default:
			ident.val = ident.symbol.getTemp();
			break;
		}
	}
	
	@Override
	public void visitBreak(Tree.Break breakStmt) {
		tr.genBranch(loopExits.peek());
	}

	@Override
	public void visitCallExpr(Tree.CallExpr callExpr) {
		if (callExpr.isArrayLength) {
			callExpr.receiver.accept(this);
			callExpr.val = tr.genLoad(callExpr.receiver.val,
					-OffsetCounter.WORD_SIZE, false);
		} else {
			if (callExpr.receiver != null) {
				callExpr.receiver.accept(this);
			}
			for (Tree.Expr expr : callExpr.actuals) {
				expr.accept(this);
			}
			if (callExpr.receiver != null) {
				tr.genParm(callExpr.receiver.val);
			}
			for (Tree.Expr expr : callExpr.actuals) {
				tr.genParm(expr.val);
			}
			if (callExpr.receiver == null) {
				callExpr.val = tr.genDirectCall(
						callExpr.symbol.getFuncty().label, callExpr.symbol
								.getReturnType());
			} else {
				//System.out.println("genInDirectCall");
				//Temp vt = tr.genLoad(callExpr.receiver.val, 0, false); // VTable of current object
				if (callExpr.receiver instanceof Tree.SuperExpr) {
					//VTable funpvt = callExpr.getScope().getScope().getOwner().getParent().getVtable();
					VTable funpvt = tr.getCurrentFuncty().sym.getScope().getOwner().getParent().getVtable();
					Temp pvt = tr.genLoadVTable(funpvt);
					//tr.genStore(pvt, callExpr.receiver.val, 0);
					Temp func = tr.genLoad(pvt, callExpr.symbol.getOffset(), false);
					callExpr.val = tr.genIndirectCall(func, callExpr.symbol
							.getReturnType());
					//tr.genStore(vt, callExpr.receiver.val, 0);
				} else if (callExpr.receiver instanceof Tree.ThisExpr) {
					VTable funvt = tr.getCurrentFuncty().sym.getScope().getOwner().getVtable();
					Temp vt = tr.genLoadVTable(funvt);
					Temp func = tr.genLoad(vt, callExpr.symbol.getOffset(), false);
					callExpr.val = tr.genIndirectCall(func, callExpr.symbol
							.getReturnType());
				} else {
					Temp vt = tr.genLoad(callExpr.receiver.val, 0, false);
					Temp func = tr.genLoad(vt, callExpr.symbol.getOffset(), false);
					callExpr.val = tr.genIndirectCall(func, callExpr.symbol
						.getReturnType());
				}
			}
		}

	}

	@Override
	public void visitForLoop(Tree.ForLoop forLoop) {
		if (forLoop.init != null) {
			forLoop.init.accept(this);
		}
		Label cond = Label.createLabel();
		Label loop = Label.createLabel();
		tr.genBranch(cond);
		tr.genMark(loop);
		if (forLoop.update != null) {
			forLoop.update.accept(this);
		}
		tr.genMark(cond);
		forLoop.condition.accept(this);
		Label exit = Label.createLabel();
		tr.genBeqz(forLoop.condition.val, exit);
		loopExits.push(exit);
		if (forLoop.loopBody != null) {
			forLoop.loopBody.accept(this);
		}
		tr.genBranch(loop);
		loopExits.pop();
		tr.genMark(exit);
	}

	@Override
	public void visitIf(Tree.If ifStmt) {
		ifStmt.condition.accept(this);
		if (ifStmt.falseBranch != null) {
			Label falseLabel = Label.createLabel();
			tr.genBeqz(ifStmt.condition.val, falseLabel);
			ifStmt.trueBranch.accept(this);
			Label exit = Label.createLabel();
			tr.genBranch(exit);
			tr.genMark(falseLabel);
			ifStmt.falseBranch.accept(this);
			tr.genMark(exit);
		} else if (ifStmt.trueBranch != null) {
			Label exit = Label.createLabel();
			tr.genBeqz(ifStmt.condition.val, exit);
			if (ifStmt.trueBranch != null) {
				ifStmt.trueBranch.accept(this);
			}
			tr.genMark(exit);
		}
	}

	@Override
	public void visitNewArray(Tree.NewArray newArray) {
		newArray.length.accept(this);
		newArray.val = tr.genNewArray(newArray.length.val, newArray.elementType.type.equal(BaseType.COMPLEX));
	}

	@Override
	public void visitNewClass(Tree.NewClass newClass) {
		newClass.val = tr.genDirectCall(newClass.symbol.getNewFuncLabel(),
				BaseType.INT);
	}

	@Override
	public void visitWhileLoop(Tree.WhileLoop whileLoop) {
		Label loop = Label.createLabel();
		tr.genMark(loop);
		whileLoop.condition.accept(this);
		Label exit = Label.createLabel();
		tr.genBeqz(whileLoop.condition.val, exit);
		loopExits.push(exit);
		if (whileLoop.loopBody != null) {
			whileLoop.loopBody.accept(this);
		}
		tr.genBranch(loop);
		loopExits.pop();
		tr.genMark(exit);
	}

	@Override
	public void visitTypeTest(Tree.TypeTest typeTest) {
		typeTest.instance.accept(this);
		typeTest.val = tr.genInstanceof(typeTest.instance.val,
				typeTest.symbol);
	}

	@Override
	public void visitTypeCast(Tree.TypeCast typeCast) {
		typeCast.expr.accept(this);
		if (!typeCast.expr.type.compatible(typeCast.symbol.getType())) {
			tr.genClassCast(typeCast.expr.val, typeCast.symbol);
		}
		typeCast.val = typeCast.expr.val;
	}

	@Override
	public void visitCase(Tree.Case that) {
		that.condition.accept(this);
		Label exit = Label.createLabel();
		Temp value;
		if (that.defaultExpr.type.equal(BaseType.COMPLEX)) {
			value = new ComplexTemp();
		} else {
			value = Temp.createTempI4();
		}
		int len = that.caseConstList.size();
		for (int i = 0; i < len; ++ i) {
			Tree.Expr con = that.caseConstList.get(i);
			Tree.Expr exp = that.caseExprList.get(i);
			con.accept(this);
			exp.accept(this);
			tr.genAssign(value, exp.val);
			Temp cmp = tr.genSub(con.val, that.condition.val);
			tr.genBeqz(cmp, exit);
		}
		that.defaultExpr.accept(this);
		tr.genAssign(value, that.defaultExpr.val);
		tr.genMark(exit);
		that.val = value;
	}

	@Override
	public void visitPrintComp(Tree.PrintComp that) {
		int len = that.exprs.size();
		for (int i = 0; i < len; ++ i) {
			that.exprs.get(i).accept(this);
			tr.genPrintComp((ComplexTemp) that.exprs.get(i).val);
		}
	}

	/*
	@Override
	public void visitThisExpr(Tree.ThisExpr thisExpr) {
		thisExpr.val = currentThis;
	}
	*/

	@Override
	public void visitSuperExpr(Tree.SuperExpr superExpr) {
		superExpr.val = currentThis;
		//callExpr.symbol.getScope().getOwner().getVtable(); 
	}

	@Override 
	public void visitSCopyExpr(Tree.SCopyExpr expr) {
		expr.expr.accept(this);
		expr.val = tr.genSCopy(expr.expr);
	}

	@Override
	public void visitDCopyExpr(Tree.DCopyExpr expr) {
		expr.expr.accept(this);
		expr.val = tr.genDCopy(expr.expr.val, ((ClassType) expr.expr.type).getSymbol());
	}

	/*
	@Override
	public void visitWhileLoop(Tree.WhileLoop whileLoop) {
		Label loop = Label.createLabel();
		tr.genMark(loop);
		whileLoop.condition.accept(this);
		Label exit = Label.createLabel();
		tr.genBeqz(whileLoop.condition.val, exit);
		loopExits.push(exit);
		if (whileLoop.loopBody != null) {
			whileLoop.loopBody.accept(this);
		}
		tr.genBranch(loop);
		loopExits.pop();
		tr.genMark(exit);
	}
	*/

	@Override
	public void visitDoOdLoop(Tree.DoOdLoop that) {
		Label loop = Label.createLabel();
		tr.genMark(loop);
		Label exit = Label.createLabel();
		loopExits.push(exit);

		int len = that.exprList.size();
		for (int i = 0; i < len; ++ i) {
			that.exprList.get(i).accept(this);
			Label sin = Label.createLabel();
			Label sout = Label.createLabel();
			tr.genBeqz(that.exprList.get(i).val, sout);
			tr.genMark(sin);
			that.stmtList.get(i).accept(this);
			tr.genBranch(loop);
			tr.genMark(sout);
		}

		loopExits.pop();
		tr.genMark(exit);
	}

}
