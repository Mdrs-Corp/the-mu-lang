import values
import customTypes


def interpret(vars, node):
    if node.type == customTypes.NodeType.EXPRESSION:
        last = None
        for nd in node.childs:
            last = interpret(vars, nd)
        return last
    
    elif node.type == customTypes.NodeType.ACTION:
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
        if node.action == "yield":
            if node.left.type == customTypes.NodeType.IDENTIFIER:
                print(interpret(vars, node.left).value)
            else:
                print(f"Invalid variable name")

    elif node.type == customTypes.NodeType.PRINT:
        for name in vars:
            print(name, ":", vars[name].toPrint())

    elif node.type == customTypes.NodeType.OPERATOR:
        left = interpret(vars, node.left)
        right = interpret(vars, node.right)
        if node.operator == "+":return values.create(left.add(right))
        if node.operator == "*":return values.create(left.mul(right))
        if node.operator == "/":return values.create(left.div(right))

    elif node.type == customTypes.NodeType.LITERAL:
        return values.create(node.value)

    elif node.type == customTypes.NodeType.IDENTIFIER:
        if node.text in vars:
            return vars[node.text]
        print(f"{node.text} doesn't exist")
