from .decl import *
from .stmt import *
from .expr import *


class ASTPrinter:
    def __init__(self, show_node_id: bool = False):
        self.show_node_id = show_node_id
        self.lines: list[str] = []

    def format(self, node) -> str:
        self.lines = []
        self._visit(node, 0)
        return "\n".join(self.lines)

    def print(self, node) -> None:
        print(self.format(node))

    def _emit(self, indent: int, text: str) -> None:
        self.lines.append("  " * indent + text)

    def _label(self, node, name: str) -> str:
        if self.show_node_id:
            return f"{name}(id={node.node_id})"
        return name

    def _visit(self, node, indent: int) -> None:
        if node is None:
            self._emit(indent, "None")
            return

        if isinstance(node, Program):
            self._emit(indent, self._label(node, "Program"))
            self._visit(node.functions, indent + 1)

        elif isinstance(node, FunctionList):
            self._emit(indent, self._label(node, "FunctionList"))
            for func in node.functions:
                self._visit(func, indent + 1)

        elif isinstance(node, FunctionDecl):
            label = f"FunctionDecl(name: {node.name})"
            self._emit(indent, self._label(node, label))

            self._emit(indent + 1, "Parameters")
            self._visit(node.parameters, indent + 2)

            self._emit(indent + 1, "LocalVariables")
            self._visit(node.local_variables, indent + 2)

            self._emit(indent + 1, "Body")
            self._visit(node.body, indent + 2)

            self._emit(indent + 1, "Return")
            self._visit(node.return_expr, indent + 2)

        elif isinstance(node, ParamList):
            self._emit(indent, self._label(node, "ParamList"))
            for p in node.parameters:
                self._visit(p, indent + 1)

        elif isinstance(node, LocalVarDeclList):
            self._emit(indent, self._label(node, "LocalVarDeclList"))
            for d in node.declarations:
                self._visit(d, indent + 1)

        elif isinstance(node, VarDecl):
            label = f"VarDecl(name: {node.name})"
            self._emit(indent, self._label(node, label))

        elif isinstance(node, StmtList):
            self._emit(indent, self._label(node, "StmtList"))
            for stmt in node.statements:
                self._visit(stmt, indent + 1)

        elif isinstance(node, AssignStmt):
            self._emit(indent, self._label(node, "AssignStmt"))
            self._emit(indent + 1, "LHS")
            self._visit(node.lhs, indent + 2)
            self._emit(indent + 1, "RHS")
            self._visit(node.rhs, indent + 2)

        elif isinstance(node, PointerAssignStmt):
            self._emit(indent, self._label(node, "PointerAssignStmt"))
            self._emit(indent + 1, "Pointer")
            self._visit(node.pointer, indent + 2)
            self._emit(indent + 1, "Value")
            self._visit(node.value, indent + 2)

        elif isinstance(node, OutputStmt):
            self._emit(indent, self._label(node, "OutputStmt"))
            self._visit(node.value, indent + 1)

        elif isinstance(node, IfStmt):
            self._emit(indent, self._label(node, "IfStmt"))

            self._emit(indent + 1, "Condition")
            self._visit(node.condition, indent + 2)

            self._emit(indent + 1, "Then")
            self._visit(node.then_statements, indent + 2)

            self._emit(indent + 1, "Else")
            self._visit(node.else_statements, indent + 2)

        elif isinstance(node, WhileStmt):
            self._emit(indent, self._label(node, "WhileStmt"))

            self._emit(indent + 1, "Condition")
            self._visit(node.condition, indent + 2)

            self._emit(indent + 1, "Body")
            self._visit(node.statements, indent + 2)

        elif isinstance(node, IntExpr):
            label = f"IntExpr(value: {node.value})"
            self._emit(indent, self._label(node, label))

        elif isinstance(node, IdentifierExpr):
            label = f"IdentifierExpr(name: {node.name})"
            self._emit(indent, self._label(node, label))

        elif isinstance(node, InputExpr):
            self._emit(indent, self._label(node, "InputExpr"))

        elif isinstance(node, BinaryExpr):
            label = f"BinaryExpr(op: {node.op})"
            self._emit(indent, self._label(node, label))

            self._emit(indent + 1, "Left")
            self._visit(node.left, indent + 2)

            self._emit(indent + 1, "Right")
            self._visit(node.right, indent + 2)

        elif isinstance(node, NegExpr):
            self._emit(indent, self._label(node, "NegExpr"))
            self._visit(node.operand, indent + 1)

        elif isinstance(node, ArgumentList):
            self._emit(indent, self._label(node, "ArgumentList"))
            for arg in node.arguments:
                self._visit(arg, indent + 1)

        elif isinstance(node, CallExpr):
            self._emit(indent, self._label(node, "CallExpr"))
            self._emit(indent + 1, "Callee")
            self._visit(node.callee, indent + 2)
            self._emit(indent + 1, "Arguments")
            self._visit(node.arguments, indent + 2)

        elif isinstance(node, AllocExpr):
            self._emit(indent, self._label(node, "AllocExpr"))
            self._visit(node.operand, indent + 1)

        elif isinstance(node, AddressOfExpr):
            self._emit(indent, self._label(node, "AddressOfExpr"))
            self._visit(node.operand, indent + 1)

        elif isinstance(node, DerefExpr):
            self._emit(indent, self._label(node, "DerefExpr"))
            self._visit(node.operand, indent + 1)

        elif isinstance(node, NullExpr):
            self._emit(indent, self._label(node, "NullExpr"))

        else:
            raise TypeError(f"Unknown node type: {type(node).__name__}")