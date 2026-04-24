from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from .base import ASTNode, Stmt
from .expr import Expr, IdentifierExpr


@dataclass
class AssignStmt(Stmt):
    lhs: IdentifierExpr
    rhs: Expr


@dataclass
class PointerAssignStmt(Stmt):
    pointer: Expr
    value: Expr


@dataclass
class OutputStmt(Stmt):
    value: Expr


@dataclass
class StmtList(ASTNode):
    statements: List[Stmt] = field(default_factory=list)


@dataclass
class IfStmt(Stmt):
    condition: Expr
    then_statements: StmtList
    else_statements: Optional[StmtList] = None


@dataclass
class WhileStmt(Stmt):
    condition: Expr
    statements: StmtList