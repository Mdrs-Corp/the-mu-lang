from enum import Enum
import customTypes

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


class Action(Node):
    def __init__(self, action, left, right):
        super().__init__(customTypes.NodeType.ACTION)
        self.action = action
        self.left = left
        self.right = right


class Operator(Node):
    def __init__(self, operator, left, right):
        super().__init__(customTypes.NodeType.OPERATOR)
        self.operator = operator
        self.left = left
        self.right = right


class Print(Node):
    def __init__(self, operator, left, right):
        super().__init__(customTypes.NodeType.PRINT)



def parse(tokens):
    print(tokens)
    if len(tokens) == 0: return

    #each line
    if tokens[0].type == customTypes.TokenType.SEPARATOR and\
        tokens[0].text == "@" and tokens[-1].type == customTypes.TokenType.SEPARATOR and tokens[-1].text == "@":
        ind = 1
        toks = []
        nodes = []
        while ind<len(tokens)-1:
            if (tokens[ind].type == customTypes.TokenType.SEPARATOR and tokens[ind].text == "@"):
                toks.append(tokens[ind])
                ind+=1
                while not(tokens[ind].type == customTypes.TokenType.SEPARATOR and tokens[ind].text == "@"):
                    toks.append(tokens[ind])
                    ind += 1
                toks.append(tokens[ind])
                ind += 1

            if (tokens[ind].type == customTypes.TokenType.SEPARATOR and tokens[ind].text == "."):
                nodes.append(parse(toks))
                toks = []
            else:
                toks.append(tokens[ind])
            ind += 1
        if len(toks)!=0:
            nodes.append(parse(toks))
        return Expression(nodes)

    #single tokens
    if len(tokens) == 1:
        if tokens[0].type == customTypes.TokenType.IDENTIFIER:
            return Identifier(tokens[0].text)
        if tokens[0].type == customTypes.TokenType.LITERAL:
            return Literal(tokens[0].text)

    #keywords
    if tokens[0].type == customTypes.TokenType.KEYWORD:
        if tokens[0].text == "set":
            return Action(tokens[0].text, parse([tokens[1]]), parse(tokens[2:]))
        if tokens[0].text == "yield":
            return Action(tokens[0].text, parse(tokens[1:]), None)
        if tokens[0].text == "whether":
            return Action(tokens[0].text, parse([tokens[1]]), parse(tokens[2:]))

    if tokens[1].type == customTypes.TokenType.OPERATOR:
        return Operator(tokens[1].text, parse([tokens[0]]), parse(tokens[2:]))

    return "wsh t koi"
