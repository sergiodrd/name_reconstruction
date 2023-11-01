import sys

sys.path.extend([".", ".."])

from pycparser import c_ast, parse_file 


class Visitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        fn_name = node.decl.name
        fn_args = '\n\t'.join(list(map(lambda x: x.name, node.decl.type.args.params)))
        variables = '\n\t'.join(list(map(lambda x: x.name, list(filter(lambda x: isinstance(x, c_ast.Decl), node.body.block_items)))))
        print(f"Function name: {fn_name}\nFunction arguments:\n\t{fn_args}\nVariables:\n\t{variables}")


def main():
    if len(sys.argv) != 2:
        print("Please provide a c file path.")
        exit(1)

    ast = parse_file(sys.argv[1], use_cpp=True)

    # print("\n=== FULL AST ===\n")
    #
    # ast.show()
    #
    # print("\n=== FUNC DEFS ===\n")

    v = Visitor()
    v.visit(ast)
