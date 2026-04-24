from antlr4 import InputStream, CommonTokenStream
from antlr.Tip_grammarLexer import Tip_grammarLexer
from antlr.Tip_grammarParser import Tip_grammarParser

from myast.visitor import ASTVisitor
from myast.printer import ASTPrinter

from type.constraint_visitor import ConstraintVisitor
from type.constraint_printer import ConstraintPrinter
from type.type import *


source = """
compare(m, n) {
    var answer;

    if (m < n) {
        answer = n * 3;
    } else {
        answer = m * 5;
    }

    return answer ;
}

main() {
    var a, b, c, x, y, z;
    a = input ;
    *a = 7;
    b = alloc a ;
    c = null ;
    c = &b;

    x = 3;
    y = 7;

    z = compare(x,y);
    return z;
}
"""
print("===== source code =====")
print(source)

lexer = Tip_grammarLexer(InputStream(source))
tokens = CommonTokenStream(lexer)
parser = Tip_grammarParser(tokens)
parse_tree = parser.program()

visitor = ASTVisitor()
ast = visitor.visit(parse_tree)

print("===== AST =====")
printer = ASTPrinter()
printer.print(ast)

