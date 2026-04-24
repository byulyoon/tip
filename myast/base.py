from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ASTNode:  
    node_id: Optional[int] = field(default=None, init=False)

@dataclass
class Expr(ASTNode):
    pass

@dataclass
class Stmt(ASTNode):
    pass
