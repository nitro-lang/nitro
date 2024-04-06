from sly import Parser
from nitro_lexer import NitroLexer

class NitroParser(Parser):
    # Get the token list from the lexer (required)
    tokens = NitroLexer.tokens

    precedence = (
          ('nonassoc', SEMICOLON),  # Nonassociative operators
          ('left', PLUS, MINUS),
          ('left', ASTERISK, SLASH)
    )

    # Grammar rules and actions

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

    @_('expr SEMICOLON expr')
    def expr(self, p):
        return (p.expr0,p.expr1)