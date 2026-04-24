# Generated from Tip_grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Tip_grammarParser import Tip_grammarParser
else:
    from Tip_grammarParser import Tip_grammarParser

# This class defines a complete generic visitor for a parse tree produced by Tip_grammarParser.

class Tip_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Tip_grammarParser#program.
    def visitProgram(self, ctx:Tip_grammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#function.
    def visitFunction(self, ctx:Tip_grammarParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#paramList.
    def visitParamList(self, ctx:Tip_grammarParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#param.
    def visitParam(self, ctx:Tip_grammarParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#localVarDecl.
    def visitLocalVarDecl(self, ctx:Tip_grammarParser.LocalVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#assignStmt.
    def visitAssignStmt(self, ctx:Tip_grammarParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#outputStmt.
    def visitOutputStmt(self, ctx:Tip_grammarParser.OutputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#ifStatement.
    def visitIfStatement(self, ctx:Tip_grammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#whileStatement.
    def visitWhileStatement(self, ctx:Tip_grammarParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#pointerAssignStmt.
    def visitPointerAssignStmt(self, ctx:Tip_grammarParser.PointerAssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#ifStmt.
    def visitIfStmt(self, ctx:Tip_grammarParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#thenBlock.
    def visitThenBlock(self, ctx:Tip_grammarParser.ThenBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#elsePart.
    def visitElsePart(self, ctx:Tip_grammarParser.ElsePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#elseBlock.
    def visitElseBlock(self, ctx:Tip_grammarParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#whileStmt.
    def visitWhileStmt(self, ctx:Tip_grammarParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#block.
    def visitBlock(self, ctx:Tip_grammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#argList.
    def visitArgList(self, ctx:Tip_grammarParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#intExpr.
    def visitIntExpr(self, ctx:Tip_grammarParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#addSubExpr.
    def visitAddSubExpr(self, ctx:Tip_grammarParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#nullExpr.
    def visitNullExpr(self, ctx:Tip_grammarParser.NullExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#allocExpr.
    def visitAllocExpr(self, ctx:Tip_grammarParser.AllocExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#inputExpr.
    def visitInputExpr(self, ctx:Tip_grammarParser.InputExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#parenExpr.
    def visitParenExpr(self, ctx:Tip_grammarParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#addressOfExpr.
    def visitAddressOfExpr(self, ctx:Tip_grammarParser.AddressOfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#derefExpr.
    def visitDerefExpr(self, ctx:Tip_grammarParser.DerefExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#callExpr.
    def visitCallExpr(self, ctx:Tip_grammarParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:Tip_grammarParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#negNumExpr.
    def visitNegNumExpr(self, ctx:Tip_grammarParser.NegNumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#idExpr.
    def visitIdExpr(self, ctx:Tip_grammarParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Tip_grammarParser#compareExpr.
    def visitCompareExpr(self, ctx:Tip_grammarParser.CompareExprContext):
        return self.visitChildren(ctx)



del Tip_grammarParser