from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from .base import ASTNode
from .expr import Expr
from .stmt import StmtList


@dataclass
class VarDecl(ASTNode):
    name: str


@dataclass
class ParamList(ASTNode):
    parameters: List[VarDecl] = field(default_factory=list)


@dataclass
class LocalVarDeclList(ASTNode):
    declarations: List[VarDecl] = field(default_factory=list)


@dataclass
class FunctionDecl(ASTNode):
    name: str
    return_expr: Expr
    parameters: ParamList = field(default_factory=ParamList)
    local_variables: Optional[LocalVarDeclList] = None
    body: StmtList = field(default_factory=StmtList)


@dataclass
class FunctionList(ASTNode):
    functions: List[FunctionDecl] = field(default_factory=list)


@dataclass
class Program(ASTNode):
    functions: FunctionList = field(default_factory=FunctionList)