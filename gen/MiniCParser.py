# Generated from ./grammar/MiniC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,40,8,1,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,72,8,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,1,8,1,8,1,9,1,9,1,9,1,
        9,3,9,104,8,9,1,9,1,9,1,9,1,9,3,9,110,8,9,1,10,1,10,3,10,114,8,10,
        1,11,1,11,1,11,1,11,3,11,120,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,3,12,131,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,5,12,146,8,12,10,12,12,12,149,9,12,
        1,12,0,1,24,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,3,1,0,16,17,2,
        0,13,13,18,18,1,0,19,24,161,0,30,1,0,0,0,2,35,1,0,0,0,4,53,1,0,0,
        0,6,55,1,0,0,0,8,59,1,0,0,0,10,64,1,0,0,0,12,73,1,0,0,0,14,79,1,
        0,0,0,16,89,1,0,0,0,18,109,1,0,0,0,20,113,1,0,0,0,22,119,1,0,0,0,
        24,130,1,0,0,0,26,29,3,2,1,0,27,29,3,4,2,0,28,26,1,0,0,0,28,27,1,
        0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,
        30,1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,0,35,36,5,1,0,0,36,39,5,25,0,
        0,37,38,5,2,0,0,38,40,3,24,12,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,
        1,0,0,0,41,42,5,3,0,0,42,3,1,0,0,0,43,44,3,6,3,0,44,45,5,3,0,0,45,
        54,1,0,0,0,46,47,3,8,4,0,47,48,5,3,0,0,48,54,1,0,0,0,49,54,3,10,
        5,0,50,54,3,12,6,0,51,54,3,16,8,0,52,54,3,14,7,0,53,43,1,0,0,0,53,
        46,1,0,0,0,53,49,1,0,0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,
        0,54,5,1,0,0,0,55,56,5,25,0,0,56,57,5,2,0,0,57,58,3,24,12,0,58,7,
        1,0,0,0,59,60,5,4,0,0,60,61,5,5,0,0,61,62,3,24,12,0,62,63,5,6,0,
        0,63,9,1,0,0,0,64,65,5,7,0,0,65,66,5,5,0,0,66,67,3,24,12,0,67,68,
        5,6,0,0,68,71,3,4,2,0,69,70,5,8,0,0,70,72,3,4,2,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,11,1,0,0,0,73,74,5,9,0,0,74,75,5,5,0,0,75,76,3,
        24,12,0,76,77,5,6,0,0,77,78,3,4,2,0,78,13,1,0,0,0,79,80,5,10,0,0,
        80,81,5,5,0,0,81,82,3,18,9,0,82,83,5,3,0,0,83,84,3,20,10,0,84,85,
        5,3,0,0,85,86,3,22,11,0,86,87,5,6,0,0,87,88,3,4,2,0,88,15,1,0,0,
        0,89,94,5,11,0,0,90,93,3,2,1,0,91,93,3,4,2,0,92,90,1,0,0,0,92,91,
        1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,
        96,94,1,0,0,0,97,98,5,12,0,0,98,17,1,0,0,0,99,100,5,1,0,0,100,103,
        5,25,0,0,101,102,5,2,0,0,102,104,3,24,12,0,103,101,1,0,0,0,103,104,
        1,0,0,0,104,110,1,0,0,0,105,106,5,25,0,0,106,107,5,2,0,0,107,110,
        3,24,12,0,108,110,1,0,0,0,109,99,1,0,0,0,109,105,1,0,0,0,109,108,
        1,0,0,0,110,19,1,0,0,0,111,114,3,24,12,0,112,114,1,0,0,0,113,111,
        1,0,0,0,113,112,1,0,0,0,114,21,1,0,0,0,115,116,5,25,0,0,116,117,
        5,2,0,0,117,120,3,24,12,0,118,120,1,0,0,0,119,115,1,0,0,0,119,118,
        1,0,0,0,120,23,1,0,0,0,121,122,6,12,-1,0,122,123,5,13,0,0,123,131,
        3,24,12,9,124,125,5,5,0,0,125,126,3,24,12,0,126,127,5,6,0,0,127,
        131,1,0,0,0,128,131,5,26,0,0,129,131,5,25,0,0,130,121,1,0,0,0,130,
        124,1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,131,147,1,0,0,0,132,
        133,10,6,0,0,133,134,7,0,0,0,134,146,3,24,12,7,135,136,10,5,0,0,
        136,137,7,1,0,0,137,146,3,24,12,6,138,139,10,4,0,0,139,140,7,2,0,
        0,140,146,3,24,12,5,141,142,10,8,0,0,142,146,5,14,0,0,143,144,10,
        7,0,0,144,146,5,15,0,0,145,132,1,0,0,0,145,135,1,0,0,0,145,138,1,
        0,0,0,145,141,1,0,0,0,145,143,1,0,0,0,146,149,1,0,0,0,147,145,1,
        0,0,0,147,148,1,0,0,0,148,25,1,0,0,0,149,147,1,0,0,0,14,28,30,39,
        53,71,92,94,103,109,113,119,130,145,147
    ]

class MiniCParser ( Parser ):

    grammarFileName = "MiniC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'='", "';'", "'print'", "'('", 
                     "')'", "'if'", "'else'", "'while'", "'for'", "'{'", 
                     "'}'", "'-'", "'++'", "'--'", "'*'", "'/'", "'+'", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "WS", "COMMENT", "MCOMMENT" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_stmt = 2
    RULE_assign = 3
    RULE_printStmt = 4
    RULE_ifStmt = 5
    RULE_whileStmt = 6
    RULE_forStmt = 7
    RULE_block = 8
    RULE_forInital = 9
    RULE_forCondition = 10
    RULE_forStep = 11
    RULE_expr = 12

    ruleNames =  [ "program", "decl", "stmt", "assign", "printStmt", "ifStmt", 
                   "whileStmt", "forStmt", "block", "forInital", "forCondition", 
                   "forStep", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    ID=25
    NUMBER=26
    WS=27
    COMMENT=28
    MCOMMENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniCParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniCParser.DeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33558162) != 0):
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 26
                    self.decl()
                    pass
                elif token in [4, 7, 9, 10, 11, 25]:
                    self.state = 27
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(MiniCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(MiniCParser.T__0)
            self.state = 36
            self.match(MiniCParser.ID)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 37
                self.match(MiniCParser.T__1)
                self.state = 38
                self.expr(0)


            self.state = 41
            self.match(MiniCParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(MiniCParser.AssignContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(MiniCParser.PrintStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniCParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MiniCParser.WhileStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniCParser.BlockContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiniCParser.ForStmtContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.assign()
                self.state = 44
                self.match(MiniCParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.printStmt()
                self.state = 47
                self.match(MiniCParser.T__2)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.ifStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.whileStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.block()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.forStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniCParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(MiniCParser.ID)
            self.state = 56
            self.match(MiniCParser.T__1)
            self.state = 57
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = MiniCParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(MiniCParser.T__3)
            self.state = 60
            self.match(MiniCParser.T__4)
            self.state = 61
            self.expr(0)
            self.state = 62
            self.match(MiniCParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MiniCParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MiniCParser.T__6)
            self.state = 65
            self.match(MiniCParser.T__4)
            self.state = 66
            self.expr(0)
            self.state = 67
            self.match(MiniCParser.T__5)
            self.state = 68
            self.stmt()
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 69
                self.match(MiniCParser.T__7)
                self.state = 70
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MiniCParser.StmtContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MiniCParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MiniCParser.T__8)
            self.state = 74
            self.match(MiniCParser.T__4)
            self.state = 75
            self.expr(0)
            self.state = 76
            self.match(MiniCParser.T__5)
            self.state = 77
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forInital(self):
            return self.getTypedRuleContext(MiniCParser.ForInitalContext,0)


        def forCondition(self):
            return self.getTypedRuleContext(MiniCParser.ForConditionContext,0)


        def forStep(self):
            return self.getTypedRuleContext(MiniCParser.ForStepContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MiniCParser.StmtContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MiniCParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MiniCParser.T__9)
            self.state = 80
            self.match(MiniCParser.T__4)
            self.state = 81
            self.forInital()
            self.state = 82
            self.match(MiniCParser.T__2)
            self.state = 83
            self.forCondition()
            self.state = 84
            self.match(MiniCParser.T__2)
            self.state = 85
            self.forStep()
            self.state = 86
            self.match(MiniCParser.T__5)
            self.state = 87
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniCParser.DeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MiniCParser.T__10)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33558162) != 0):
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 90
                    self.decl()
                    pass
                elif token in [4, 7, 9, 10, 11, 25]:
                    self.state = 91
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(MiniCParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniCParser.RULE_forInital

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForInitDeclContext(ForInitalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ForInitalContext
            super().__init__(parser)
            self.id_ = None # Token
            self.e = None # ExprContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitDecl" ):
                listener.enterForInitDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitDecl" ):
                listener.exitForInitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitDecl" ):
                return visitor.visitForInitDecl(self)
            else:
                return visitor.visitChildren(self)


    class ForInitAssignContext(ForInitalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ForInitalContext
            super().__init__(parser)
            self.id_ = None # Token
            self.e = None # ExprContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitAssign" ):
                listener.enterForInitAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitAssign" ):
                listener.exitForInitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitAssign" ):
                return visitor.visitForInitAssign(self)
            else:
                return visitor.visitChildren(self)


    class ForInitEmptyContext(ForInitalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ForInitalContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitEmpty" ):
                listener.enterForInitEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitEmpty" ):
                listener.exitForInitEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitEmpty" ):
                return visitor.visitForInitEmpty(self)
            else:
                return visitor.visitChildren(self)



    def forInital(self):

        localctx = MiniCParser.ForInitalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forInital)
        self._la = 0 # Token type
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MiniCParser.ForInitDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(MiniCParser.T__0)
                self.state = 100
                localctx.id_ = self.match(MiniCParser.ID)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 101
                    self.match(MiniCParser.T__1)
                    self.state = 102
                    localctx.e = self.expr(0)


                pass
            elif token in [25]:
                localctx = MiniCParser.ForInitAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                localctx.id_ = self.match(MiniCParser.ID)
                self.state = 106
                self.match(MiniCParser.T__1)
                self.state = 107
                localctx.e = self.expr(0)
                pass
            elif token in [3]:
                localctx = MiniCParser.ForInitEmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniCParser.RULE_forCondition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForCondEmptyContext(ForConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ForConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondEmpty" ):
                listener.enterForCondEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondEmpty" ):
                listener.exitForCondEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondEmpty" ):
                return visitor.visitForCondEmpty(self)
            else:
                return visitor.visitChildren(self)


    class ForCondExprContext(ForConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ForConditionContext
            super().__init__(parser)
            self.e = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondExpr" ):
                listener.enterForCondExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondExpr" ):
                listener.exitForCondExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondExpr" ):
                return visitor.visitForCondExpr(self)
            else:
                return visitor.visitChildren(self)



    def forCondition(self):

        localctx = MiniCParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forCondition)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 13, 25, 26]:
                localctx = MiniCParser.ForCondExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                localctx.e = self.expr(0)
                pass
            elif token in [3]:
                localctx = MiniCParser.ForCondEmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniCParser.RULE_forStep

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStepEmptyContext(ForStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ForStepContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStepEmpty" ):
                listener.enterForStepEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStepEmpty" ):
                listener.exitForStepEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStepEmpty" ):
                return visitor.visitForStepEmpty(self)
            else:
                return visitor.visitChildren(self)


    class ForStepAssignContext(ForStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ForStepContext
            super().__init__(parser)
            self.id_ = None # Token
            self.e = None # ExprContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStepAssign" ):
                listener.enterForStepAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStepAssign" ):
                listener.exitForStepAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStepAssign" ):
                return visitor.visitForStepAssign(self)
            else:
                return visitor.visitChildren(self)



    def forStep(self):

        localctx = MiniCParser.ForStepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forStep)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = MiniCParser.ForStepAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                localctx.id_ = self.match(MiniCParser.ID)
                self.state = 116
                self.match(MiniCParser.T__1)
                self.state = 117
                localctx.e = self.expr(0)
                pass
            elif token in [6]:
                localctx = MiniCParser.ForStepEmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniCParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class PostfixminusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixminus" ):
                listener.enterPostfixminus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixminus" ):
                listener.exitPostfixminus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixminus" ):
                return visitor.visitPostfixminus(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(MiniCParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class PostfixaddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixadd" ):
                listener.enterPostfixadd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixadd" ):
                listener.exitPostfixadd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixadd" ):
                return visitor.visitPostfixadd(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniCParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class CmpExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniCParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmpExpr" ):
                listener.enterCmpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmpExpr" ):
                listener.exitCmpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmpExpr" ):
                return visitor.visitCmpExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = MiniCParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 122
                self.match(MiniCParser.T__12)
                self.state = 123
                self.expr(9)
                pass
            elif token in [5]:
                localctx = MiniCParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(MiniCParser.T__4)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(MiniCParser.T__5)
                pass
            elif token in [26]:
                localctx = MiniCParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(MiniCParser.NUMBER)
                pass
            elif token in [25]:
                localctx = MiniCParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.match(MiniCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 145
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MiniCParser.MulDivExprContext(self, MiniCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 133
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MiniCParser.AddSubExprContext(self, MiniCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 135
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 136
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 137
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = MiniCParser.CmpExprContext(self, MiniCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 138
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 139
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 140
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = MiniCParser.PostfixaddContext(self, MiniCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 142
                        self.match(MiniCParser.T__13)
                        pass

                    elif la_ == 5:
                        localctx = MiniCParser.PostfixminusContext(self, MiniCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 143
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 144
                        self.match(MiniCParser.T__14)
                        pass

             
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         




