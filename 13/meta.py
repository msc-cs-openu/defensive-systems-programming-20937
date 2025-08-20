import ast
from types import CodeType


class MethodInjector(ast.NodeTransformer):
    def __init__(self, code_to_add):
        self.code_to_add = code_to_add

    def visit_FunctionDef(self, node):
        if node.name.startswith("__") and node.name.endswith("__"):
            new_code = ast.parse(self.code_to_add).body
            node.body.extend(new_code)
        return node


def modify_class_code(file_name: str, code_to_add: str) -> CodeType:
    with open(file_name, "r") as file:
        tree = ast.parse(file.read())

    injector = MethodInjector(code_to_add)

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            injector.visit(node)
    ast.fix_missing_locations(tree)

    return compile(tree, filename="<ast>", mode="exec")


def main():
    file_name = input("Enter python file name: ")
    py_code = input("Enter python code: ")

    try:
        modified_code = modify_class_code(file_name, py_code)

        exec(modified_code, globals())

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
