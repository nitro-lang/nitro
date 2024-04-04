from nitro_token import TokenType,Token

class Lexer():
    def __init__(self, source:str) -> None:
        self.source = source

        self.position = -1
        self.read_position = 0
        self.line_number = 1

        self.current_char : str | None = None

        self.read_char()

    def read_char(self) -> None:
        if self.read_position >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def next_token(self) -> Token:
        Tok : Token = None

        


