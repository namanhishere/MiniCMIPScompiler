
grammar MiniC;

// Entry
program : (decl | stmt)* EOF ;

// Declarations
decl : 'int' ID ('=' expr)? ';' ;

// Statements
stmt
    : assign ';'
    | printStmt ';'
    | ifStmt
    | whileStmt
    | block
    | forStmt
    ;

assign : ID '=' expr ;
printStmt : 'print' '(' expr ')' ;

ifStmt : 'if' '(' expr ')' stmt ('else' stmt)? ;
whileStmt : 'while' '(' expr ')' stmt ;
forStmt : 'for' '(' forInital ';' forCondition ';' forStep  ')' stmt  ;
block : '{' (decl | stmt)* '}' ;


forInital
    : 'int' id=ID ('=' e=expr)?      #forInitDecl
    | id=ID '=' e=expr               #forInitAssign
    |                                 #forInitEmpty
    ;

forCondition
    : e=expr                          #forCondExpr
    |                                  #forCondEmpty
    ;

forStep
    : id=ID '=' e=expr                #forStepAssign
    |                                  #forStepEmpty
    ;

// Expressions with ANTLR4 direct left recursion (supported)
expr
    : '-' expr                               #unaryMinusExpr
    | expr '++'                              #postfixadd
    | expr '--'                              #postfixminus
    | expr op=('*'|'/') expr                 #mulDivExpr
    | expr op=('+'|'-') expr                 #addSubExpr
    | expr op=('<' | '<=' | '>' | '>=' | '==' | '!=') expr  #cmpExpr
    | '(' expr ')'                           #parenExpr
    | NUMBER                                 #numberExpr
    | ID                                     #idExpr
    ;





ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
MCOMMENT: '/*' .*? '*/' -> skip ;
