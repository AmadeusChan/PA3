Exception in thread "main" java.lang.NullPointerException
	at decaf.typecheck.TypeCheck.checkBinaryOp(TypeCheck.java:583)
	at decaf.typecheck.TypeCheck.visitBinary(TypeCheck.java:65)
	at decaf.tree.Tree$Binary.accept(Tree.java:985)
	at decaf.typecheck.TypeCheck.checkCallExpr(TypeCheck.java:173)
	at decaf.typecheck.TypeCheck.visitCallExpr(TypeCheck.java:239)
	at decaf.tree.Tree$CallExpr.accept(Tree.java:1056)
	at decaf.typecheck.TypeCheck.visitExec(TypeCheck.java:244)
	at decaf.tree.Tree$Exec.accept(Tree.java:667)
	at decaf.typecheck.TypeCheck.visitBlock(TypeCheck.java:433)
	at decaf.tree.Tree$Block.accept(Tree.java:521)
	at decaf.typecheck.TypeCheck.visitMethodDef(TypeCheck.java:416)
	at decaf.tree.Tree$MethodDef.accept(Tree.java:441)
	at decaf.typecheck.TypeCheck.visitClassDef(TypeCheck.java:407)
	at decaf.tree.Tree$ClassDef.accept(Tree.java:406)
	at decaf.typecheck.TypeCheck.visitTopLevel(TypeCheck.java:424)
	at decaf.typecheck.TypeCheck.checkType(TypeCheck.java:60)
	at decaf.Driver.compile(Driver.java:95)
	at decaf.Driver.main(Driver.java:117)
