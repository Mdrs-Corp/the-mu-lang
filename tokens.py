from enum import Enum

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "-.0123456789"

def lex(string):
    tokens = []
    currentPos = 0
    while currentPos < len(string):
        tokenStartPos = currentPos
        lookahead = string[currentPos]
        if lookahead == " ":
            currentPos += 1
        elif lookahead == '+':
            currentPos += 1
            tokens.append(Token(TokenType.PLUS, lookahead, tokenStartPos))
        elif lookahead == '*':
            currentPos += 1
            tokens.append(Token(TokenType.TIMES, lookahead, tokenStartPos))
        elif lookahead in "-.0123456789":
            text = ""
            while currentPos < len(string) and string[currentPos] in numbers:
                text += string[currentPos]
                currentPos += 1
            tokens.append(Token(TokenType.NUMBER, text, tokenStartPos))
        elif lookahead in letters:
            text = ""
            while currentPos < len(string) and (string[currentPos] in letters or string[currentPos] in numbers):
                text += string[currentPos]
                currentPos += 1
            if text == "true":
                type = TokenType.TRUE
            elif text == "false":
                type = TokenType.FALSE
            else:
                type = TokenType.IDENTIFIER
            tokens.append(Token(type, text, tokenStartPos))
        else:
            print(f"Unknown character '{lookahead}' at position {currentPos}")
    tokens.append(Token(TokenType.EOF, "<EOF>", currentPos))
    return tokens


class TokenType(Enum):
    EOF = 0
    IDENTIFIER = 1
    NUMBER = 2
    TRUE = 3
    FALSE = 4
    PLUS = 5
    TIMES = 6

class Token:
    def __init__(self, type, text, pos):
        self.type = type
        self.text = text
        self.pos = pos

    def __repr__(self):
        return "<"+str(self.type)+" "+str(self.text)+" "+str(self.pos)+">"
