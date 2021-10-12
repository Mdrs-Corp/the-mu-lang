from enum import Enum

class NodeType(Enum):
    EXPR = 0
    MAKE = 1
    SET = 2
    IDENTIFIER = 3
    OPERATOR = 4
    LITERAL = 5
    PRINT = 6
    ACTION = 7
    EXPRESSION = 8

class TokenType(Enum):
    IDENTIFIER = 0
    KEYWORD = 1
    LITERAL = 2
    OPERATOR = 3
    SEPARATOR = 4
