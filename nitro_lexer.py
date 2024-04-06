from sly import Lexer

class NitroLexer(Lexer):
    # token names
    tokens = { ID, NUMBER, PLUS, MINUS, ASTERISK, SLASH, POWER, ASSIGN, LPAREN, RPAREN, SEMICOLON }

    # ignore whitespace
    ignore = ' \t'

    # ignore comment
    ignore_comment = r'\#.*'

    # regular expression rules for tokens
    ID          = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER      = r'\d+'
    PLUS        = r'\+'
    MINUS       = r'-'
    ASTERISK    = r'\*'
    SLASH       = r'/'
    POWER       = r'\^'
    ASSIGN      = r'='
    LPAREN      = r'\('
    RPAREN      = r'\)'
    SEMICOLON   = r'\;'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)   # Convert to a numeric value
        return t
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1
