from nitro_globals import *
from nitro_lexer import NitroLexer
from sly import Parser
import logging


class NitroParser(Parser):

    log = logging.getLogger()
    log.disabled = True

    tokens = NitroLexer.tokens

    precedence = (
          ('nonassoc', SEMICOLON),
          ('left', PLUS, MINUS),
          ('left', ASTERISK, SLASH)
    )

    # Grammar rules and actions

    def error(self, p):
        if p:
            self.errok()
        else:
            print(f"{warning_color}WARNING{reset_color} : Reached error EOF")

    
    @_('expr SEMICOLON')
    def instruction(self, p):
        return [p[0]]
    
    @_('var SEMICOLON')
    def instruction(self, p):
        return [p[0]]
        
    @_('function')
    def instruction(self, p):
        return [p[0]]

    @_('instruction instruction')
    def instruction(self, p):
        return p[0] + p[1]
    
    @_('expr COMMA')
    def parameter(self, p):
        return [p[0]]

    @_('parameter parameter')
    def parameter(self, p):
        return p[0] + p[1]

    @_('expr PLUS expr')
    def expr(self, p):
        return ("add",p[0],p[2])

    @_('expr MINUS expr')
    def expr(self, p):
        return ("sub",p[0],p[2])

    @_('expr ASTERISK expr')
    def expr(self, p):
        return ("mul",p[0],p[2])

    @_('expr SLASH expr')
    def expr(self, p):
        return ("div",p[0],p[2])

    @_('NUMBER')
    def expr(self, p):
        return p[0]
    
    @_('STRING')
    def expr(self, p):
        return p[0]

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p[1]

    @_('VAR ID')
    def var(self, p):
        return ("var",p[1],None,None)
    
    @_('VAR ID COLON ID')
    def var(self, p):
        return ("var",p[1],None,p[3])

    @_('VAR ID ASSIGN expr')
    def var(self, p):
        return ("var",p[1],p[3],None)
    
    @_('VAR ID COLON ID ASSIGN expr')
    def var(self, p):
        return ("var",p[1],p[5],p[3])

    @_('expr')
    def argument(self, p):
        return [("arg",p[0],None)]
    
    @_('expr COLON ID')
    def argument(self, p):
        return [("arg",p[0],p[2])]

    @_('argument COMMA argument')
    def argument(self, p):
        return p[0] + p[2]

    @_('FUNC ID LPAREN RPAREN LBRACE instruction RBRACE')
    def function(self, p):
        return ("func",p[1],None,p[5])
    
    @_('FUNC ID LPAREN argument RPAREN LBRACE instruction RBRACE')
    def function(self, p):
        return ("func",p[1],p[3],p[6])
    
    @_('ID LPAREN argument RPAREN')
    def expr(self, p):
        return ("call",p[0],p[2])

    @_('ID LPAREN RPAREN')
    def expr(self, p):
        return ("call",p[0],None)
    
    @_('ID')
    def expr(self, p):
        return ("get",p[0])
    