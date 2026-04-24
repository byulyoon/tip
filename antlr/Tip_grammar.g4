grammar Tip_grammar;

program
    : function* EOF
    ;

function
    : ID '(' paramList? ')' '{' localVarDecl* stmt* 'return' expr ';' '}'
    ;

paramList
    : param (',' param)*
    ;

param
    : ID
    ;

localVarDecl
    : 'var' ID (',' ID)* ';'
    ;

stmt
    : ID '=' expr ';'                  # assignStmt
    | 'output' expr ';'                # outputStmt
    | ifStmt                           # ifStatement
    | whileStmt                        # whileStatement
    | '*' expr '=' expr ';'            # pointerAssignStmt
    ;

ifStmt
    : 'if' '(' expr ')' thenBlock elsePart?
    ;

thenBlock
    : '{' stmt* '}'
    ;

elsePart
    : 'else' elseBlock
    ;

elseBlock
    : '{' stmt* '}'
    ;

whileStmt
    : 'while' '(' expr ')' block
    ;

block
    : '{' stmt* '}'
    ;

argList
    : expr (',' expr)*
    ;

expr
    : '(' expr ')'                         # parenExpr
    | expr '(' argList? ')'                # callExpr
    | '*' expr                             # derefExpr
    | expr ('*' | '/') expr                # mulDivExpr
    | expr ('+' | '-') expr                # addSubExpr
    | expr ('>' | '<' | '>=' | '<=' | '==') expr   # compareExpr
    | '-' expr                             # negNumExpr
    | INT                                  # intExpr
    | ID                                   # idExpr
    | 'input'                              # inputExpr
    | 'alloc' expr                         # allocExpr
    | '&' expr                             # addressOfExpr
    | 'null'                               # nullExpr
    ;

ID : [a-zA-Z]+;
INT : [0-9]+;
WS : [ \t\r\n]+ -> skip;