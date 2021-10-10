from enum import Enum

class NodeType(Enum):
    EXPR = 0
    MAKE = 1
    SET = 2
    IDENTIFIER = 3
    OPERATOR = 4
    LITERAL = 5

class TokenType(Enum):
    EOF = 0
    EOL = 1
    IDENTIFIER = 2
    KEYWORD = 3
    LITERAL = 4
    OPERATOR = 5
    SEPARATOR = 6
