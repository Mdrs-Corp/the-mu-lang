from enum import Enum
import customTypes


def parse(tokens):
    if len(tokens) == 1:
        if tokens[0].type == customTypes.TokenType.IDENTIFIER:
            return Identifier(tokens[0].text)
        if tokens[0].type == customTypes.TokenType.LITERAL:
            return Literal(tokens[0].text)
    if tokens[0].type == customTypes.TokenType.KEYWORD:
        if tokens[0].text == "make":
            return Make(parse([tokens[1]]), parse(tokens[2:]))
        if tokens[0].text == "set":
            return Set(parse([tokens[1]]), parse(tokens[2:]))

    pos = 1
    ctokens = [tokens[0]]
    if tokens[0].type == customTypes.TokenType.SEPARATOR:
        if tokens[0].text == "(":
            ctokens = []
            while tokens[pos].text != ")" or pos>len(tokens):
                ctokens.append(tokens[pos])
                pos += 1
            pos += 1
    if pos<len(tokens):
        if tokens[pos].type == customTypes.TokenType.OPERATOR:
            return Operator(tokens[pos].text, parse(ctokens), parse(tokens[pos+1:]))
    else:
        return parse(ctokens)




class Node:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        ls = self.__dict__
        return str([str(i)+": "+str(ls[i]) for i in ls])

class Identifier(Node):
    def __init__(self, text):
        super().__init__(customTypes.NodeType.IDENTIFIER)
        self.text = text


class Literal(Node):
    def __init__(self, value):
        super().__init__(customTypes.NodeType.LITERAL)
        self.value = value

class Expression(Node):
    def __init__(self, nodes = []):
        super().__init__(customTypes.NodeType.EXPRESSION)
        self.childs = []
        for i in nodes:
            self.addNode(i)

    def addNode(self, node):
        self.childs.append(node)

class Make(Node):
    def __init__(self, type, name):
        super().__init__(customTypes.NodeType.MAKE)
        self.left = type
        self.right = name


class Set(Node):
    def __init__(self, name, value):
        super().__init__(customTypes.NodeType.SET)
        self.left = name
        self.right = value


class Operator(Node):
    def __init__(self, operator, left, right):
        super().__init__(customTypes.NodeType.OPERATOR)
        self.operator = operator
        self.left = left
        self.right = right
