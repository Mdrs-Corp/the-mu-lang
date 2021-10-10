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
        elif lookahead == '+' or lookahead == '*':
            currentPos += 1
            tokens.append(Token(TokenType.OPERATOR, lookahead, tokenStartPos))
        elif lookahead in "-.0123456789":
            text = ""
            while currentPos < len(string) and string[currentPos] in numbers:
                text += string[currentPos]
                currentPos += 1
            tokens.append(Token(TokenType.NUMBER, text, tokenStartPos))
        elif lookahead == "\"" or lookahead == "'":
            text = ""
            currentPos += 1
            while currentPos < len(string) and not(string[currentPos] == "\"" or string[currentPos] == "'" ):
                text += string[currentPos]
                currentPos += 1
            currentPos += 1
            tokens.append(Token(TokenType.STRING, text, tokenStartPos))
        elif lookahead in letters:
            text = ""
            while currentPos < len(string) and (string[currentPos] in letters or string[currentPos] in numbers):
                text += string[currentPos]
                currentPos += 1
            if text == "true" or text == "false":
                type = TokenType.BOOLEAN
            elif text == "make" or text == "set":
                type = TokenType.KEYWORD
            else:
                type = TokenType.IDENTIFIER
            tokens.append(Token(type, text, tokenStartPos))
        elif lookahead == "\n":
            tokens.append(Token(TokenType.EOL, lookahead, tokenStartPos))
            currentPos += 1
        else:
            print(f"Unknown character '{lookahead}' at position {currentPos}")
            currentPos += 1
    tokens.append(Token(TokenType.EOF, "<EOF>", currentPos))
    return tokens


class TokenType(Enum):
    EOF = 0
    EOL = 1
    IDENTIFIER = 2
    KEYWORD = 3
    LITERAL = 4
    OPERATOR = 5

class Token:
    def __init__(self, type, text, pos):
        self.type = type
        self.text = text
        self.pos = pos

    def __repr__(self):
        return "<"+str(self.type)+" "+repr(self.text)+" "+str(self.pos)+">"
