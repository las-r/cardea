from .nodes import *

# cardea emitter
# made by las-r on github

class emitter:
    def emit(self, ast):
        # boilerplate
        code = "#include <stdio.h>\n"
        code += "#include <stdbool.h>\n\n"
        code += "int main() {\n"
        
        for statement in ast.body:
            # print
            if isinstance(statement, printnode):
                node = statement.value
                if node.type == "str": code += f'printf("%s\\n", {node.value});\n'
                elif node.type in ["int", "bit"]: code += f'printf("%d\\n", {node.value});\n'
                elif node.type == "flt": code += f'printf("%f\\n", {node.value});\n'
        
        code += "return 0;\n"
        code += "}\n"
        return code