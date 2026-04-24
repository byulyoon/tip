# Generated from Tip_grammar.g4 by ANTLR 4.13.2
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
        4,1,29,192,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,1,1,3,1,40,8,1,1,
        1,1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,2,
        1,3,1,3,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,99,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,107,8,6,1,7,1,7,5,7,111,8,
        7,10,7,12,7,114,9,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,5,9,123,8,9,10,9,
        12,9,126,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,5,11,
        138,8,11,10,11,12,11,141,9,11,1,11,1,11,1,12,1,12,1,12,5,12,148,
        8,12,10,12,12,12,151,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,170,8,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,184,
        8,13,1,13,5,13,187,8,13,10,13,12,13,190,9,13,1,13,0,1,26,14,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,0,3,2,0,11,11,15,15,1,0,16,17,1,
        0,18,22,205,0,31,1,0,0,0,2,36,1,0,0,0,4,60,1,0,0,0,6,68,1,0,0,0,
        8,70,1,0,0,0,10,98,1,0,0,0,12,100,1,0,0,0,14,108,1,0,0,0,16,117,
        1,0,0,0,18,120,1,0,0,0,20,129,1,0,0,0,22,135,1,0,0,0,24,144,1,0,
        0,0,26,169,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,33,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,0,0,
        1,35,1,1,0,0,0,36,37,5,27,0,0,37,39,5,1,0,0,38,40,3,4,2,0,39,38,
        1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,2,0,0,42,46,5,3,0,0,
        43,45,3,8,4,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,
        0,0,0,47,52,1,0,0,0,48,46,1,0,0,0,49,51,3,10,5,0,50,49,1,0,0,0,51,
        54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,
        0,55,56,5,4,0,0,56,57,3,26,13,0,57,58,5,5,0,0,58,59,5,6,0,0,59,3,
        1,0,0,0,60,65,3,6,3,0,61,62,5,7,0,0,62,64,3,6,3,0,63,61,1,0,0,0,
        64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,5,1,0,0,0,67,65,1,0,
        0,0,68,69,5,27,0,0,69,7,1,0,0,0,70,71,5,8,0,0,71,76,5,27,0,0,72,
        73,5,7,0,0,73,75,5,27,0,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,
        0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,5,0,0,80,9,
        1,0,0,0,81,82,5,27,0,0,82,83,5,9,0,0,83,84,3,26,13,0,84,85,5,5,0,
        0,85,99,1,0,0,0,86,87,5,10,0,0,87,88,3,26,13,0,88,89,5,5,0,0,89,
        99,1,0,0,0,90,99,3,12,6,0,91,99,3,20,10,0,92,93,5,11,0,0,93,94,3,
        26,13,0,94,95,5,9,0,0,95,96,3,26,13,0,96,97,5,5,0,0,97,99,1,0,0,
        0,98,81,1,0,0,0,98,86,1,0,0,0,98,90,1,0,0,0,98,91,1,0,0,0,98,92,
        1,0,0,0,99,11,1,0,0,0,100,101,5,12,0,0,101,102,5,1,0,0,102,103,3,
        26,13,0,103,104,5,2,0,0,104,106,3,14,7,0,105,107,3,16,8,0,106,105,
        1,0,0,0,106,107,1,0,0,0,107,13,1,0,0,0,108,112,5,3,0,0,109,111,3,
        10,5,0,110,109,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,
        0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,116,5,6,0,0,116,15,1,0,
        0,0,117,118,5,13,0,0,118,119,3,18,9,0,119,17,1,0,0,0,120,124,5,3,
        0,0,121,123,3,10,5,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,
        0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,6,
        0,0,128,19,1,0,0,0,129,130,5,14,0,0,130,131,5,1,0,0,131,132,3,26,
        13,0,132,133,5,2,0,0,133,134,3,22,11,0,134,21,1,0,0,0,135,139,5,
        3,0,0,136,138,3,10,5,0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,1,
        0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,143,5,
        6,0,0,143,23,1,0,0,0,144,149,3,26,13,0,145,146,5,7,0,0,146,148,3,
        26,13,0,147,145,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,25,1,0,0,0,151,149,1,0,0,0,152,153,6,13,-1,0,153,154,
        5,1,0,0,154,155,3,26,13,0,155,156,5,2,0,0,156,170,1,0,0,0,157,158,
        5,11,0,0,158,170,3,26,13,11,159,160,5,17,0,0,160,170,3,26,13,7,161,
        170,5,28,0,0,162,170,5,27,0,0,163,170,5,23,0,0,164,165,5,24,0,0,
        165,170,3,26,13,3,166,167,5,25,0,0,167,170,3,26,13,2,168,170,5,26,
        0,0,169,152,1,0,0,0,169,157,1,0,0,0,169,159,1,0,0,0,169,161,1,0,
        0,0,169,162,1,0,0,0,169,163,1,0,0,0,169,164,1,0,0,0,169,166,1,0,
        0,0,169,168,1,0,0,0,170,188,1,0,0,0,171,172,10,10,0,0,172,173,7,
        0,0,0,173,187,3,26,13,11,174,175,10,9,0,0,175,176,7,1,0,0,176,187,
        3,26,13,10,177,178,10,8,0,0,178,179,7,2,0,0,179,187,3,26,13,9,180,
        181,10,12,0,0,181,183,5,1,0,0,182,184,3,24,12,0,183,182,1,0,0,0,
        183,184,1,0,0,0,184,185,1,0,0,0,185,187,5,2,0,0,186,171,1,0,0,0,
        186,174,1,0,0,0,186,177,1,0,0,0,186,180,1,0,0,0,187,190,1,0,0,0,
        188,186,1,0,0,0,188,189,1,0,0,0,189,27,1,0,0,0,190,188,1,0,0,0,16,
        31,39,46,52,65,76,98,106,112,124,139,149,169,183,186,188
    ]

class Tip_grammarParser ( Parser ):

    grammarFileName = "Tip_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'return'", "';'", 
                     "'}'", "','", "'var'", "'='", "'output'", "'*'", "'if'", 
                     "'else'", "'while'", "'/'", "'+'", "'-'", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'input'", "'alloc'", "'&'", 
                     "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "WS" ]

    RULE_program = 0
    RULE_function = 1
    RULE_paramList = 2
    RULE_param = 3
    RULE_localVarDecl = 4
    RULE_stmt = 5
    RULE_ifStmt = 6
    RULE_thenBlock = 7
    RULE_elsePart = 8
    RULE_elseBlock = 9
    RULE_whileStmt = 10
    RULE_block = 11
    RULE_argList = 12
    RULE_expr = 13

    ruleNames =  [ "program", "function", "paramList", "param", "localVarDecl", 
                   "stmt", "ifStmt", "thenBlock", "elsePart", "elseBlock", 
                   "whileStmt", "block", "argList", "expr" ]

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
    T__24=25
    T__25=26
    ID=27
    INT=28
    WS=29

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
            return self.getToken(Tip_grammarParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.FunctionContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.FunctionContext,i)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_program

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

        localctx = Tip_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 28
                self.function()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(Tip_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Tip_grammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def paramList(self):
            return self.getTypedRuleContext(Tip_grammarParser.ParamListContext,0)


        def localVarDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.LocalVarDeclContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.LocalVarDeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.StmtContext,i)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = Tip_grammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(Tip_grammarParser.ID)
            self.state = 37
            self.match(Tip_grammarParser.T__0)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 38
                self.paramList()


            self.state = 41
            self.match(Tip_grammarParser.T__1)
            self.state = 42
            self.match(Tip_grammarParser.T__2)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 43
                self.localVarDecl()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134241280) != 0):
                self.state = 49
                self.stmt()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(Tip_grammarParser.T__3)
            self.state = 56
            self.expr(0)
            self.state = 57
            self.match(Tip_grammarParser.T__4)
            self.state = 58
            self.match(Tip_grammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.ParamContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.ParamContext,i)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = Tip_grammarParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.param()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 61
                self.match(Tip_grammarParser.T__6)
                self.state = 62
                self.param()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Tip_grammarParser.ID, 0)

        def getRuleIndex(self):
            return Tip_grammarParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = Tip_grammarParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(Tip_grammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Tip_grammarParser.ID)
            else:
                return self.getToken(Tip_grammarParser.ID, i)

        def getRuleIndex(self):
            return Tip_grammarParser.RULE_localVarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVarDecl" ):
                listener.enterLocalVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVarDecl" ):
                listener.exitLocalVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalVarDecl" ):
                return visitor.visitLocalVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def localVarDecl(self):

        localctx = Tip_grammarParser.LocalVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_localVarDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(Tip_grammarParser.T__7)
            self.state = 71
            self.match(Tip_grammarParser.ID)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 72
                self.match(Tip_grammarParser.T__6)
                self.state = 73
                self.match(Tip_grammarParser.ID)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(Tip_grammarParser.T__4)
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


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStmt(self):
            return self.getTypedRuleContext(Tip_grammarParser.WhileStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Tip_grammarParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class OutputStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputStmt" ):
                listener.enterOutputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputStmt" ):
                listener.exitOutputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStmt" ):
                return visitor.visitOutputStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStmt(self):
            return self.getTypedRuleContext(Tip_grammarParser.IfStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)


    class PointerAssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerAssignStmt" ):
                listener.enterPointerAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerAssignStmt" ):
                listener.exitPointerAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointerAssignStmt" ):
                return visitor.visitPointerAssignStmt(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = Tip_grammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = Tip_grammarParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(Tip_grammarParser.ID)
                self.state = 82
                self.match(Tip_grammarParser.T__8)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(Tip_grammarParser.T__4)
                pass
            elif token in [10]:
                localctx = Tip_grammarParser.OutputStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(Tip_grammarParser.T__9)
                self.state = 87
                self.expr(0)
                self.state = 88
                self.match(Tip_grammarParser.T__4)
                pass
            elif token in [12]:
                localctx = Tip_grammarParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.ifStmt()
                pass
            elif token in [14]:
                localctx = Tip_grammarParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.whileStmt()
                pass
            elif token in [11]:
                localctx = Tip_grammarParser.PointerAssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.match(Tip_grammarParser.T__10)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(Tip_grammarParser.T__8)
                self.state = 95
                self.expr(0)
                self.state = 96
                self.match(Tip_grammarParser.T__4)
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


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def thenBlock(self):
            return self.getTypedRuleContext(Tip_grammarParser.ThenBlockContext,0)


        def elsePart(self):
            return self.getTypedRuleContext(Tip_grammarParser.ElsePartContext,0)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_ifStmt

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

        localctx = Tip_grammarParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(Tip_grammarParser.T__11)
            self.state = 101
            self.match(Tip_grammarParser.T__0)
            self.state = 102
            self.expr(0)
            self.state = 103
            self.match(Tip_grammarParser.T__1)
            self.state = 104
            self.thenBlock()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 105
                self.elsePart()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThenBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.StmtContext,i)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_thenBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThenBlock" ):
                listener.enterThenBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThenBlock" ):
                listener.exitThenBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThenBlock" ):
                return visitor.visitThenBlock(self)
            else:
                return visitor.visitChildren(self)




    def thenBlock(self):

        localctx = Tip_grammarParser.ThenBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_thenBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(Tip_grammarParser.T__2)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134241280) != 0):
                self.state = 109
                self.stmt()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(Tip_grammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsePartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseBlock(self):
            return self.getTypedRuleContext(Tip_grammarParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_elsePart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsePart" ):
                listener.enterElsePart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsePart" ):
                listener.exitElsePart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsePart" ):
                return visitor.visitElsePart(self)
            else:
                return visitor.visitChildren(self)




    def elsePart(self):

        localctx = Tip_grammarParser.ElsePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elsePart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(Tip_grammarParser.T__12)
            self.state = 118
            self.elseBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.StmtContext,i)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = Tip_grammarParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(Tip_grammarParser.T__2)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134241280) != 0):
                self.state = 121
                self.stmt()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(Tip_grammarParser.T__5)
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
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(Tip_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_whileStmt

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

        localctx = Tip_grammarParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(Tip_grammarParser.T__13)
            self.state = 130
            self.match(Tip_grammarParser.T__0)
            self.state = 131
            self.expr(0)
            self.state = 132
            self.match(Tip_grammarParser.T__1)
            self.state = 133
            self.block()
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.StmtContext,i)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_block

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

        localctx = Tip_grammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(Tip_grammarParser.T__2)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134241280) != 0):
                self.state = 136
                self.stmt()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(Tip_grammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.ExprContext,i)


        def getRuleIndex(self):
            return Tip_grammarParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = Tip_grammarParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.expr(0)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 145
                self.match(Tip_grammarParser.T__6)
                self.state = 146
                self.expr(0)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return Tip_grammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(Tip_grammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.ExprContext,i)


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


    class NullExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullExpr" ):
                listener.enterNullExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullExpr" ):
                listener.exitNullExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullExpr" ):
                return visitor.visitNullExpr(self)
            else:
                return visitor.visitChildren(self)


    class AllocExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllocExpr" ):
                listener.enterAllocExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllocExpr" ):
                listener.exitAllocExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllocExpr" ):
                return visitor.visitAllocExpr(self)
            else:
                return visitor.visitChildren(self)


    class InputExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputExpr" ):
                listener.enterInputExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputExpr" ):
                listener.exitInputExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputExpr" ):
                return visitor.visitInputExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


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


    class AddressOfExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddressOfExpr" ):
                listener.enterAddressOfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddressOfExpr" ):
                listener.exitAddressOfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddressOfExpr" ):
                return visitor.visitAddressOfExpr(self)
            else:
                return visitor.visitChildren(self)


    class DerefExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDerefExpr" ):
                listener.enterDerefExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDerefExpr" ):
                listener.exitDerefExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDerefExpr" ):
                return visitor.visitDerefExpr(self)
            else:
                return visitor.visitChildren(self)


    class CallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)

        def argList(self):
            return self.getTypedRuleContext(Tip_grammarParser.ArgListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpr" ):
                listener.enterCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpr" ):
                listener.exitCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.ExprContext,i)


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


    class NegNumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Tip_grammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegNumExpr" ):
                listener.enterNegNumExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegNumExpr" ):
                listener.exitNegNumExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegNumExpr" ):
                return visitor.visitNegNumExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Tip_grammarParser.ID, 0)

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


    class CompareExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Tip_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Tip_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(Tip_grammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Tip_grammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = Tip_grammarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 153
                self.match(Tip_grammarParser.T__0)
                self.state = 154
                self.expr(0)
                self.state = 155
                self.match(Tip_grammarParser.T__1)
                pass
            elif token in [11]:
                localctx = Tip_grammarParser.DerefExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(Tip_grammarParser.T__10)
                self.state = 158
                self.expr(11)
                pass
            elif token in [17]:
                localctx = Tip_grammarParser.NegNumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(Tip_grammarParser.T__16)
                self.state = 160
                self.expr(7)
                pass
            elif token in [28]:
                localctx = Tip_grammarParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.match(Tip_grammarParser.INT)
                pass
            elif token in [27]:
                localctx = Tip_grammarParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(Tip_grammarParser.ID)
                pass
            elif token in [23]:
                localctx = Tip_grammarParser.InputExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.match(Tip_grammarParser.T__22)
                pass
            elif token in [24]:
                localctx = Tip_grammarParser.AllocExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                self.match(Tip_grammarParser.T__23)
                self.state = 165
                self.expr(3)
                pass
            elif token in [25]:
                localctx = Tip_grammarParser.AddressOfExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 166
                self.match(Tip_grammarParser.T__24)
                self.state = 167
                self.expr(2)
                pass
            elif token in [26]:
                localctx = Tip_grammarParser.NullExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(Tip_grammarParser.T__25)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 186
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = Tip_grammarParser.MulDivExprContext(self, Tip_grammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 172
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 173
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = Tip_grammarParser.AddSubExprContext(self, Tip_grammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 175
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 176
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = Tip_grammarParser.CompareExprContext(self, Tip_grammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 177
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 178
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8126464) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 179
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = Tip_grammarParser.CallExprContext(self, Tip_grammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 180
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 181
                        self.match(Tip_grammarParser.T__0)
                        self.state = 183
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 528615426) != 0):
                            self.state = 182
                            self.argList()


                        self.state = 185
                        self.match(Tip_grammarParser.T__1)
                        pass

             
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         




