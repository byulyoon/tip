from .decl import *
from .stmt import *
from .expr import *
from .base import Expr as BaseExpr
from .base import Stmt as BaseStmt


class ASTFactory:
    def __init__(self):
        self._node_counter = 0

    def _set_node_id(self, node):
        self._node_counter += 1
        node.node_id = self._node_counter
        return node

    def make_program(self, functions):
        if not isinstance(functions, list):
            raise TypeError(f"functions must be list, got {type(functions).__name__}")
        for fn in functions:
            if not isinstance(fn, FunctionDecl):
                raise TypeError(
                    f"functions must contain FunctionDecl, got {type(fn).__name__}"
                )

        return self._set_node_id(
            Program(functions=self.make_function_list(functions))
        )

    def make_function_list(self, functions=None):
        functions = functions or []
        if not isinstance(functions, list):
            raise TypeError(f"functions must be list, got {type(functions).__name__}")
        for fn in functions:
            if not isinstance(fn, FunctionDecl):
                raise TypeError(
                    f"functions must contain FunctionDecl, got {type(fn).__name__}"
                )

        return self._set_node_id(
            FunctionList(functions=functions)
        )

    def make_function(self, name, return_expr, parameters=None, local_variables=None, body=None):
        if not isinstance(name, str):
            raise TypeError(f"name must be str, got {type(name).__name__}")

        if not isinstance(return_expr, BaseExpr):
            raise TypeError(f"return_expr must be Expr, got {type(return_expr).__name__}")

        if parameters is not None and not isinstance(parameters, ParamList):
            raise TypeError(f"parameters must be ParamList, got {type(parameters).__name__}")

        if local_variables is not None and not isinstance(local_variables, LocalVarDeclList):
            raise TypeError(
                f"local_variables must be LocalVarDeclList, got {type(local_variables).__name__}"
            )

        if body is not None and not isinstance(body, StmtList):
            raise TypeError(f"body must be StmtList, got {type(body).__name__}")

        return self._set_node_id(
            FunctionDecl(
                name=name,
                return_expr=return_expr,
                parameters=parameters if parameters is not None else self.make_param_list(),
                local_variables=local_variables,
                body=body if body is not None else self.make_stmt_list(),
            )
        )

    def make_param_list(self, params=None):
        params = params or []
        if not isinstance(params, list):
            raise TypeError(f"params must be list, got {type(params).__name__}")
        for p in params:
            if not isinstance(p, VarDecl):
                raise TypeError(f"params must contain VarDecl, got {type(p).__name__}")

        return self._set_node_id(
            ParamList(parameters=params)
        )

    def make_local_var_list(self, decls=None):
        decls = decls or []
        if not isinstance(decls, list):
            raise TypeError(f"decls must be list, got {type(decls).__name__}")
        for d in decls:
            if not isinstance(d, VarDecl):
                raise TypeError(f"decls must contain VarDecl, got {type(d).__name__}")

        return self._set_node_id(
            LocalVarDeclList(declarations=decls)
        )

    def make_stmt_list(self, stmts=None):
        stmts = stmts or []
        if not isinstance(stmts, list):
            raise TypeError(f"stmts must be list, got {type(stmts).__name__}")
        for stmt in stmts:
            if not isinstance(stmt, BaseStmt):
                raise TypeError(f"stmts must contain Stmt, got {type(stmt).__name__}")

        return self._set_node_id(
            StmtList(statements=stmts)
        )

    def make_var_decl(self, name):
        if not isinstance(name, str):
            raise TypeError(f"name must be str, got {type(name).__name__}")

        return self._set_node_id(
            VarDecl(name=name)
        )

    def make_identifier(self, name):
        if not isinstance(name, str):
            raise TypeError(f"name must be str, got {type(name).__name__}")

        return self._set_node_id(
            IdentifierExpr(name=name)
        )

    def make_int(self, value):
        if not isinstance(value, int):
            raise TypeError(f"value must be int, got {type(value).__name__}")

        return self._set_node_id(
            IntExpr(value=value)
        )

    def make_input(self):
        return self._set_node_id(
            InputExpr()
        )

    def make_binary(self, op, left, right):
        if not isinstance(op, str):
            raise TypeError(f"op must be str, got {type(op).__name__}")
        if not isinstance(left, BaseExpr):
            raise TypeError(f"left must be Expr, got {type(left).__name__}")
        if not isinstance(right, BaseExpr):
            raise TypeError(f"right must be Expr, got {type(right).__name__}")

        return self._set_node_id(
            BinaryExpr(op=op, left=left, right=right)
        )

    def make_neg(self, operand):
        if not isinstance(operand, BaseExpr):
            raise TypeError(f"operand must be Expr, got {type(operand).__name__}")

        return self._set_node_id(
            NegExpr(operand=operand)
        )

    def make_arg_list(self, args=None):
        args = args or []
        if not isinstance(args, list):
            raise TypeError(f"args must be list, got {type(args).__name__}")
        for arg in args:
            if not isinstance(arg, BaseExpr):
                raise TypeError(f"args must contain Expr, got {type(arg).__name__}")

        return self._set_node_id(
            ArgumentList(arguments=args)
        )

    def make_call(self, callee, arguments=None):
        if not isinstance(callee, BaseExpr):
            raise TypeError(f"callee must be Expr, got {type(callee).__name__}")

        if arguments is None:
            arguments = self.make_arg_list()
        elif not isinstance(arguments, ArgumentList):
            raise TypeError(
                f"arguments must be ArgumentList, got {type(arguments).__name__}"
            )

        return self._set_node_id(
            CallExpr(callee=callee, arguments=arguments)
        )

    def make_assign(self, lhs, rhs):
        if not isinstance(lhs, IdentifierExpr):
            raise TypeError(
                f"lhs must be IdentifierExpr, got {type(lhs).__name__}"
            )
        if not isinstance(rhs, BaseExpr):
            raise TypeError(f"rhs must be Expr, got {type(rhs).__name__}")

        return self._set_node_id(
            AssignStmt(lhs=lhs, rhs=rhs)
        )

    def make_pointer_assign(self, pointer, value):
        if not isinstance(pointer, BaseExpr):
            raise TypeError(f"pointer must be Expr, got {type(pointer).__name__}")
        if not isinstance(value, BaseExpr):
            raise TypeError(f"value must be Expr, got {type(value).__name__}")

        return self._set_node_id(
            PointerAssignStmt(pointer=pointer, value=value)
        )

    def make_output(self, value):
        if not isinstance(value, BaseExpr):
            raise TypeError(f"value must be Expr, got {type(value).__name__}")

        return self._set_node_id(
            OutputStmt(value=value)
        )

    def make_if(self, condition, then_statements, else_statements=None):
        if not isinstance(condition, BaseExpr):
            raise TypeError(
                f"condition must be Expr, got {type(condition).__name__}"
            )
        if not isinstance(then_statements, StmtList):
            raise TypeError(
                f"then_statements must be StmtList, got {type(then_statements).__name__}"
            )
        if else_statements is not None and not isinstance(else_statements, StmtList):
            raise TypeError(
                f"else_statements must be StmtList or None, got {type(else_statements).__name__}"
            )

        return self._set_node_id(
            IfStmt(
                condition=condition,
                then_statements=then_statements,
                else_statements=else_statements,
            )
        )

    def make_while(self, condition, statements):
        if not isinstance(condition, BaseExpr):
            raise TypeError(
                f"condition must be Expr, got {type(condition).__name__}"
            )
        if not isinstance(statements, StmtList):
            raise TypeError(
                f"statements must be StmtList, got {type(statements).__name__}"
            )

        return self._set_node_id(
            WhileStmt(condition=condition, statements=statements)
        )

    def make_alloc(self, operand):
        if not isinstance(operand, BaseExpr):
            raise TypeError(f"operand must be Expr, got {type(operand).__name__}")

        return self._set_node_id(
            AllocExpr(operand=operand)
        )

    def make_address_of(self, operand):
        if not isinstance(operand, BaseExpr):
            raise TypeError(f"operand must be Expr, got {type(operand).__name__}")

        return self._set_node_id(
            AddressOfExpr(operand=operand)
        )

    def make_deref(self, operand):
        if not isinstance(operand, BaseExpr):
            raise TypeError(f"operand must be Expr, got {type(operand).__name__}")

        return self._set_node_id(
            DerefExpr(operand=operand)
        )

    def make_null(self):
        return self._set_node_id(
            NullExpr()
        )