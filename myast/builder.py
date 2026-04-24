from .decl import *
from .stmt import *
from .expr import *
from .base import Stmt as BaseStmt


class ASTBuilder:
    def __init__(self, factory):
        self.factory = factory

    def build_function(self, name, parameters, local_variables, statements, return_expr):
        if not isinstance(name, str):
            raise TypeError(f"Function name must be str, got {type(name).__name__}")

        if not isinstance(parameters, ParamList):
            raise TypeError(f"parameters must be ParamList, got {type(parameters).__name__}")

        if not isinstance(local_variables, LocalVarDeclList):
            raise TypeError(
                f"local_variables must be LocalVarDeclList, got {type(local_variables).__name__}"
            )

        if not isinstance(statements, list):
            raise TypeError(f"statements must be list, got {type(statements).__name__}")

        for stmt in statements:
            if not isinstance(stmt, BaseStmt):
                raise TypeError(
                    f"statements must contain Stmt, got {type(stmt).__name__}"
                )

        if not isinstance(return_expr, Expr):
            raise TypeError(f"return_expr must be Expr, got {type(return_expr).__name__}")

        stmt_list = self.factory.make_stmt_list(statements)

        return self.factory.make_function(
            name=name,
            return_expr=return_expr,
            parameters=parameters,
            local_variables=local_variables,
            body=stmt_list,
        )

    def build_if(self, condition, then_stmts, else_stmts):
        if not isinstance(condition, Expr):
            raise TypeError(f"condition must be Expr, got {type(condition).__name__}")

        if then_stmts is None:
            then_stmts = []

        if not isinstance(then_stmts, list):
            raise TypeError(f"then_stmts must be list, got {type(then_stmts).__name__}")

        for stmt in then_stmts:
            if not isinstance(stmt, BaseStmt):
                raise TypeError(
                    f"then_stmts must contain Stmt, got {type(stmt).__name__}"
                )

        if else_stmts is not None:
            if not isinstance(else_stmts, list):
                raise TypeError(
                    f"else_stmts must be list or None, got {type(else_stmts).__name__}"
                )

            for stmt in else_stmts:
                if not isinstance(stmt, BaseStmt):
                    raise TypeError(
                        f"else_stmts must contain Stmt, got {type(stmt).__name__}"
                    )

        then_list = self.factory.make_stmt_list(then_stmts)
        else_list = self.factory.make_stmt_list(else_stmts) if else_stmts is not None else None

        return self.factory.make_if(condition, then_list, else_list)

    def build_while(self, condition, body):
        if not isinstance(condition, Expr):
            raise TypeError(f"condition must be Expr, got {type(condition).__name__}")

        if not isinstance(body, list):
            raise TypeError(f"body must be list, got {type(body).__name__}")

        for stmt in body:
            if not isinstance(stmt, BaseStmt):
                raise TypeError(f"body must contain Stmt, got {type(stmt).__name__}")

        body_list = self.factory.make_stmt_list(body)
        return self.factory.make_while(condition, body_list)

    def build_program(self, functions):
        if not isinstance(functions, list):
            raise TypeError(f"functions must be list, got {type(functions).__name__}")

        for fn in functions:
            if not isinstance(fn, FunctionDecl):
                raise TypeError(
                    f"functions must contain FunctionDecl, got {type(fn).__name__}"
                )

        return self.factory.make_program(functions)