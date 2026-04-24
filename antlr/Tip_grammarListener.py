# Generated from Tip_grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Tip_grammarParser import Tip_grammarParser
else:
    from Tip_grammarParser import Tip_grammarParser

# This class defines a complete listener for a parse tree produced by Tip_grammarParser.
class Tip_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by Tip_grammarParser#program.
    def enterProgram(self, ctx:Tip_grammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#program.
    def exitProgram(self, ctx:Tip_grammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#function.
    def enterFunction(self, ctx:Tip_grammarParser.FunctionContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#function.
    def exitFunction(self, ctx:Tip_grammarParser.FunctionContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#paramList.
    def enterParamList(self, ctx:Tip_grammarParser.ParamListContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#paramList.
    def exitParamList(self, ctx:Tip_grammarParser.ParamListContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#param.
    def enterParam(self, ctx:Tip_grammarParser.ParamContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#param.
    def exitParam(self, ctx:Tip_grammarParser.ParamContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#localVarDecl.
    def enterLocalVarDecl(self, ctx:Tip_grammarParser.LocalVarDeclContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#localVarDecl.
    def exitLocalVarDecl(self, ctx:Tip_grammarParser.LocalVarDeclContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#assignStmt.
    def enterAssignStmt(self, ctx:Tip_grammarParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#assignStmt.
    def exitAssignStmt(self, ctx:Tip_grammarParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#outputStmt.
    def enterOutputStmt(self, ctx:Tip_grammarParser.OutputStmtContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#outputStmt.
    def exitOutputStmt(self, ctx:Tip_grammarParser.OutputStmtContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#ifStatement.
    def enterIfStatement(self, ctx:Tip_grammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#ifStatement.
    def exitIfStatement(self, ctx:Tip_grammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#whileStatement.
    def enterWhileStatement(self, ctx:Tip_grammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#whileStatement.
    def exitWhileStatement(self, ctx:Tip_grammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#pointerAssignStmt.
    def enterPointerAssignStmt(self, ctx:Tip_grammarParser.PointerAssignStmtContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#pointerAssignStmt.
    def exitPointerAssignStmt(self, ctx:Tip_grammarParser.PointerAssignStmtContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#ifStmt.
    def enterIfStmt(self, ctx:Tip_grammarParser.IfStmtContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#ifStmt.
    def exitIfStmt(self, ctx:Tip_grammarParser.IfStmtContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#thenBlock.
    def enterThenBlock(self, ctx:Tip_grammarParser.ThenBlockContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#thenBlock.
    def exitThenBlock(self, ctx:Tip_grammarParser.ThenBlockContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#elsePart.
    def enterElsePart(self, ctx:Tip_grammarParser.ElsePartContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#elsePart.
    def exitElsePart(self, ctx:Tip_grammarParser.ElsePartContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#elseBlock.
    def enterElseBlock(self, ctx:Tip_grammarParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#elseBlock.
    def exitElseBlock(self, ctx:Tip_grammarParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#whileStmt.
    def enterWhileStmt(self, ctx:Tip_grammarParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#whileStmt.
    def exitWhileStmt(self, ctx:Tip_grammarParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#block.
    def enterBlock(self, ctx:Tip_grammarParser.BlockContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#block.
    def exitBlock(self, ctx:Tip_grammarParser.BlockContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#argList.
    def enterArgList(self, ctx:Tip_grammarParser.ArgListContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#argList.
    def exitArgList(self, ctx:Tip_grammarParser.ArgListContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#intExpr.
    def enterIntExpr(self, ctx:Tip_grammarParser.IntExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#intExpr.
    def exitIntExpr(self, ctx:Tip_grammarParser.IntExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#addSubExpr.
    def enterAddSubExpr(self, ctx:Tip_grammarParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#addSubExpr.
    def exitAddSubExpr(self, ctx:Tip_grammarParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#nullExpr.
    def enterNullExpr(self, ctx:Tip_grammarParser.NullExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#nullExpr.
    def exitNullExpr(self, ctx:Tip_grammarParser.NullExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#allocExpr.
    def enterAllocExpr(self, ctx:Tip_grammarParser.AllocExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#allocExpr.
    def exitAllocExpr(self, ctx:Tip_grammarParser.AllocExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#inputExpr.
    def enterInputExpr(self, ctx:Tip_grammarParser.InputExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#inputExpr.
    def exitInputExpr(self, ctx:Tip_grammarParser.InputExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#parenExpr.
    def enterParenExpr(self, ctx:Tip_grammarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#parenExpr.
    def exitParenExpr(self, ctx:Tip_grammarParser.ParenExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#addressOfExpr.
    def enterAddressOfExpr(self, ctx:Tip_grammarParser.AddressOfExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#addressOfExpr.
    def exitAddressOfExpr(self, ctx:Tip_grammarParser.AddressOfExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#derefExpr.
    def enterDerefExpr(self, ctx:Tip_grammarParser.DerefExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#derefExpr.
    def exitDerefExpr(self, ctx:Tip_grammarParser.DerefExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#callExpr.
    def enterCallExpr(self, ctx:Tip_grammarParser.CallExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#callExpr.
    def exitCallExpr(self, ctx:Tip_grammarParser.CallExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:Tip_grammarParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:Tip_grammarParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#negNumExpr.
    def enterNegNumExpr(self, ctx:Tip_grammarParser.NegNumExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#negNumExpr.
    def exitNegNumExpr(self, ctx:Tip_grammarParser.NegNumExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#idExpr.
    def enterIdExpr(self, ctx:Tip_grammarParser.IdExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#idExpr.
    def exitIdExpr(self, ctx:Tip_grammarParser.IdExprContext):
        pass


    # Enter a parse tree produced by Tip_grammarParser#compareExpr.
    def enterCompareExpr(self, ctx:Tip_grammarParser.CompareExprContext):
        pass

    # Exit a parse tree produced by Tip_grammarParser#compareExpr.
    def exitCompareExpr(self, ctx:Tip_grammarParser.CompareExprContext):
        pass



del Tip_grammarParser