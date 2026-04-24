from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from .base import ASTNode, Expr


@dataclass
class IntExpr(Expr):
    value: int


@dataclass
class IdentifierExpr(Expr):
    name: str


@dataclass
class InputExpr(Expr):
    pass


@dataclass
class BinaryExpr(Expr):
    op: str
    left: Expr
    right: Expr


@dataclass
class NegExpr(Expr):
    operand: Expr


@dataclass
class ArgumentList(ASTNode):
    arguments: List[Expr] = field(default_factory=list)


@dataclass
class CallExpr(Expr):
    callee: Expr
    arguments: ArgumentList = field(default_factory=ArgumentList)


@dataclass
class AllocExpr(Expr):
    operand: Expr


@dataclass
class AddressOfExpr(Expr):
    operand: Expr


@dataclass
class DerefExpr(Expr):
    operand: Expr


@dataclass
class NullExpr(Expr):
    pass