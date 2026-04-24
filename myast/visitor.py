from antlr.Tip_grammarVisitor import Tip_grammarVisitor
from antlr.Tip_grammarParser import Tip_grammarParser

from .factory import ASTFactory
from .builder import ASTBuilder


class ASTVisitor(Tip_grammarVisitor):
    def __init__(self):
        self.factory = ASTFactory()
        self.builder = ASTBuilder(self.factory)

    def visit(self, tree):
        if tree is None:
            raise ValueError("Cannot visit None")

        result = super().visit(tree)

        if result is None:
            raise NotImplementedError(
                f"Unhandled parse node: {type(tree).__name__}"
            )

        return result

    def visitProgram(self, ctx: Tip_grammarParser.ProgramContext):
        functions = [self.visit(f) for f in ctx.function()]
        return self.builder.build_program(functions)

    def visitFunction(self, ctx: Tip_grammarParser.FunctionContext):
        func_name = ctx.ID().getText()

        if ctx.paramList():
            parameters = self.visit(ctx.paramList())
        else:
            parameters = self.factory.make_param_list()

        local_decls = []
        for decl_ctx in ctx.localVarDecl():
            local_decls.extend(self.visit(decl_ctx))

        local_variables = self.factory.make_local_var_list(local_decls)

        statements = [self.visit(s) for s in ctx.stmt()]
        return_expr = self.visit(ctx.expr())

        return self.builder.build_function(
            name=func_name,
            parameters=parameters,
            local_variables=local_variables,
            statements=statements,
            return_expr=return_expr,
        )

    def visitParamList(self, ctx: Tip_grammarParser.ParamListContext):
        params = [self.visit(p) for p in ctx.param()]
        return self.factory.make_param_list(params)

    def visitParam(self, ctx: Tip_grammarParser.ParamContext):
        return self.factory.make_var_decl(ctx.ID().getText())

    def visitLocalVarDecl(self, ctx: Tip_grammarParser.LocalVarDeclContext):
        ids = ctx.ID()
        if not ids:
            raise ValueError("localVarDecl must contain at least one identifier")
        return [self.factory.make_var_decl(tok.getText()) for tok in ids]

    def visitAssignStmt(self, ctx: Tip_grammarParser.AssignStmtContext):
        lhs = self.factory.make_identifier(ctx.ID().getText())
        rhs = self.visit(ctx.expr())
        return self.factory.make_assign(lhs, rhs)

    def visitPointerAssignStmt(self, ctx: Tip_grammarParser.PointerAssignStmtContext):
        pointer = self.visit(ctx.expr(0))
        value = self.visit(ctx.expr(1))
        return self.factory.make_pointer_assign(pointer, value)

    def visitOutputStmt(self, ctx: Tip_grammarParser.OutputStmtContext):
        value = self.visit(ctx.expr())
        return self.factory.make_output(value)

    def visitIfStatement(self, ctx: Tip_grammarParser.IfStatementContext):
        return self.visit(ctx.ifStmt())

    def visitIfStmt(self, ctx: Tip_grammarParser.IfStmtContext):
        condition = self.visit(ctx.expr())
        then_stmts = [self.visit(s) for s in ctx.thenBlock().stmt()]

        if ctx.elsePart():
            else_stmts = [self.visit(s) for s in ctx.elsePart().elseBlock().stmt()]
        else:
            else_stmts = None

        return self.builder.build_if(condition, then_stmts, else_stmts)

    def visitWhileStatement(self, ctx: Tip_grammarParser.WhileStatementContext):
        return self.visit(ctx.whileStmt())

    def visitWhileStmt(self, ctx: Tip_grammarParser.WhileStmtContext):
        condition = self.visit(ctx.expr())
        body = [self.visit(s) for s in ctx.block().stmt()]
        return self.builder.build_while(condition, body)

    def visitParenExpr(self, ctx: Tip_grammarParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitMulDivExpr(self, ctx: Tip_grammarParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return self.factory.make_binary(op, left, right)

    def visitAddSubExpr(self, ctx: Tip_grammarParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return self.factory.make_binary(op, left, right)

    def visitCompareExpr(self, ctx: Tip_grammarParser.CompareExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return self.factory.make_binary(op, left, right)

    def visitNegNumExpr(self, ctx: Tip_grammarParser.NegNumExprContext):
        operand = self.visit(ctx.expr())
        return self.factory.make_neg(operand)

    def visitCallExpr(self, ctx: Tip_grammarParser.CallExprContext):
        callee = self.visit(ctx.expr())
        if ctx.argList():
            arguments = self.visit(ctx.argList())
        else:
            arguments = self.factory.make_arg_list()
        return self.factory.make_call(callee, arguments)

    def visitArgList(self, ctx: Tip_grammarParser.ArgListContext):
        args = [self.visit(e) for e in ctx.expr()]
        return self.factory.make_arg_list(args)

    def visitIntExpr(self, ctx: Tip_grammarParser.IntExprContext):
        return self.factory.make_int(int(ctx.INT().getText()))

    def visitIdExpr(self, ctx: Tip_grammarParser.IdExprContext):
        return self.factory.make_identifier(ctx.ID().getText())

    def visitInputExpr(self, ctx: Tip_grammarParser.InputExprContext):
        return self.factory.make_input()

    def visitAllocExpr(self, ctx: Tip_grammarParser.AllocExprContext):
        operand = self.visit(ctx.expr())
        return self.factory.make_alloc(operand)

    def visitAddressOfExpr(self, ctx: Tip_grammarParser.AddressOfExprContext):
        operand = self.visit(ctx.expr())
        return self.factory.make_address_of(operand)

    def visitDerefExpr(self, ctx: Tip_grammarParser.DerefExprContext):
        operand = self.visit(ctx.expr())
        return self.factory.make_deref(operand)

    def visitNullExpr(self, ctx: Tip_grammarParser.NullExprContext):
        return self.factory.make_null()