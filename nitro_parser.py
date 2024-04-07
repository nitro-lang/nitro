from sly import Parser
from nitro_lexer import NitroLexer
import logging

instructions = []

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

    @_('expr SEMICOLON')
    def instruction(self, p):
        instructions.append(p.expr)

    @_('instruction instruction')
    def expr(self, p):
        instructions.extend([p.instruction0,p.instruction1])

    @_('expr PLUS expr')
    def expr(self, p):
        return ("add",p.expr0,p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return ("sub",p.expr0,p.expr1)

    @_('expr ASTERISK expr')
    def expr(self, p):
        return ("mul",p.expr0,p.expr1)

    @_('expr SLASH expr')
    def expr(self, p):
        return ("div",p.expr0,p.expr1)

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr
