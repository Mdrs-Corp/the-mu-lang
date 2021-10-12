import values
import customTypes


def interpret(vars, node):
    if node.type == customTypes.NodeType.EXPRESSION:
        for nd in node.childs:
            interpret(vars, nd)
    if node.type == customTypes.NodeType.ACTION:
        if node.action == "set":
            if node.left.type == customTypes.NodeType.IDENTIFIER:
                res = interpret(vars, node.right)
                if res==None:
                    print("Invalid value")
                else:
                    vars[node.left.text] = res
                    print(f"{node.left.text} set to {res.toPrint()}")
            else:
                print(f"Invalid variable name")

    if node.type == customTypes.NodeType.PRINT:
        for name in vars:
            print(name, ":", vars[name].toPrint())

    if node.type == customTypes.NodeType.OPERATOR:
        left = float(interpret(vars, node.left))
        right = float(interpret(vars, node.right))
        if node.operator == "+":
            return str(left + right)
        if node.operator == "*":
            return str(left * right)
        if node.operator == "/":
            return str(left / right)

    if node.type == customTypes.NodeType.LITERAL:
        return values.create(node.value)

    if node.type == customTypes.NodeType.IDENTIFIER:
        return vars[node.text]
