from enum import Enum

class TokenType(Enum):
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"

    INT = "INT"
    FLOAT = "FLOAT"

    PLUS = "PLUS"
    MINUS = "MINUS"
    ASTERISK = "ASTERISK"
    SLASH = "SLASH"
    POW = "POW"
    MODULUS = "MODULUS"

    SEMICOLON = "SEMICOLON"

    LPAREN = "LPAREN"
    RPAREN = "RPAREN"

class Token():
    def __init__(self, type:TokenType, literal:any, line_number:int, position:int) -> None:
        self.type = type
        self.literal = literal
        self.line_number = line_number
        self.position = position

    def __str__(self) -> str:
        return f"type {self.type} , literal {self.literal}"
    
    def __repr__(self) -> str:
        return str(self)
    
