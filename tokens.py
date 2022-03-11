import customTypes

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "-,0123456789"
operators = "+*/<>"

def lex(string):
    tokens = []
    currentPos = 0
    while currentPos < len(string):
        tokenStartPos = currentPos
        lookahead = string[currentPos]
        if lookahead == " " or lookahead == "\n":
            currentPos += 1
        elif lookahead in numbers:
            text = ""
            while currentPos < len(string) and string[currentPos] in numbers:
                text += string[currentPos]
                currentPos += 1
            if text == "-":
                tokens.append(Token(customTypes.TokenType.OPERATOR, text, tokenStartPos))
            tokens.append(Token(customTypes.TokenType.LITERAL, text, tokenStartPos))
        elif lookahead in operators:
            currentPos += 1
            tokens.append(Token(customTypes.TokenType.OPERATOR, lookahead, tokenStartPos))
        elif lookahead == '"' or lookahead == "'":
            text = ""
            currentPos += 1
            while currentPos < len(string) and not(string[currentPos] == '"' or string[currentPos] == "'" ):
                text += string[currentPos]
                currentPos += 1
            currentPos += 1
            tokens.append(Token(customTypes.TokenType.LITERAL, '"'+text+'"', tokenStartPos))
        elif lookahead in letters:
            text = ""
            while currentPos < len(string) and (string[currentPos] in letters or string[currentPos] in numbers):
                text += string[currentPos]
                currentPos += 1
            if text == "true" or text == "false":
                type = customTypes.TokenType.LITERAL
            elif text == "set" or text == "yield" or text == "whether" or text == "while":
                type = customTypes.TokenType.KEYWORD
            else:
                type = customTypes.TokenType.IDENTIFIER
            tokens.append(Token(type, text, tokenStartPos))
        elif lookahead == ".":
            tokens.append(Token(customTypes.TokenType.SEPARATOR, lookahead, tokenStartPos))
            currentPos += 1
        elif lookahead == "@":
            tokens.append(Token(customTypes.TokenType.SEPARATOR, lookahead, tokenStartPos))
            currentPos += 1
        else:
            print(f"Unknown character '{lookahead}' at position {currentPos}")
            currentPos += 1
    #tokens.append(Token(customTypes.TokenType.SEPARATOR, "<EOP>", currentPos))
    return tokens

class Token:
    def __init__(self, type, text, pos):
        self.type = type
        self.text = text
        self.pos = pos

    def __repr__(self):
        return "<"+str(self.type)+" "+repr(self.text)+" "+str(self.pos)+">"
