from .nodes import *

# cardea emitter
# made by las-r on github

class emitter:
    def emit(self, ast):
        code = "#include <stdio.h>\n\n"
        code += "int main() {\n"
        
        for statement in ast.body:
            if isinstance(statement, printnode):
                code += f"    printf(\"%s\\n\", {statement.value});\n"
        
        code += "    return 0;\n"
        code += "}\n"
        return code