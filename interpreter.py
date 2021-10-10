import values
import customTypes


def interpret(vars, node):
    if node.type == customTypes.NodeType.MAKE:
        if node.left.type == customTypes.NodeType.IDENTIFIER:
            var = values.create(node.left.text)
        if node.right.type == customTypes.NodeType.IDENTIFIER:
            name = node.right.text
        if var == None:
            print("Invalid type")
        elif name == None:
            print("Invalid variable name")
        else:
            vars[name] = var
            print(f"Created {name} of type {node.left.text}")

    if node.type == customTypes.NodeType.SET:
        if node.left.type == customTypes.NodeType.IDENTIFIER:
            if node.left.text in vars.keys():
                res = interpret(vars, node.right)
                success = vars[node.left.text].set(res)
                if success:
                    print(f"{node.left.text} set to {res}")
                else:
                    print("Invalid value")
            else:
                print(f"{node.left.text} not found")
        else:
            print(f"Invalid variable name")

    if node.type == customTypes.NodeType.PRINT:
        for name in vars:
            print(name, ":", vars[name].toPrint())

    if node.type == customTypes.NodeType.OPERATOR:
        left = interpret(vars, node.left)
        right = interpret(vars, node.right)
        if node.operator == "+":
            return left + right
        if node.operator == "*":
            return left * right
        if node.operator == "/":
            return left / right

    if node.type == customTypes.NodeType.LITERAL:
        return node.value

    if node.type == customTypes.NodeType.IDENTIFIER:
        return vars[node.text].value
