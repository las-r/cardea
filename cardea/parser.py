from .nodes import *

# cardea parser
# made by las-r on github

# parser
def parse(tokens):
    pos = 0
    symbols = {}
    
    # helpers
    def peek(offset=0):
        if pos + offset >= len(tokens): return None
        return tokens[pos + offset]
    
    def consume(exptype=None):
        nonlocal pos
        token = peek()
        if not token: raise RuntimeError("unexpected end of source")
        if exptype and token[0] != exptype:
            raise RuntimeError(f"expected {exptype}, got {token[0]} at {token[2]}:{token[3]}")
        pos += 1
        return token
    
    def parseexpr():
        token = consume()
        kind, val = token[0], token[1]
        
        # inferences
        if kind == "INTLIT": return LiteralNode(val, "int32")
        if kind == "FLOATLIT": return LiteralNode(val, "float32")
        if kind == "STR_LIT": return LiteralNode(val.strip('"'), "str")
        if kind == "ID":
            if val not in symbols:
                raise RuntimeError(f"undefined variable: {val}")
            return VariableRefNode(val, symbols[val])
        raise RuntimeError(f"unexcepted expression: {val}")
    
    ast = []
    while pos < len(tokens):
        token = peek()
        if token is not None:
            kind, val = token[0], token[1]
        
        # var declarations
        if val in ("const", "vola") or val in TYPEM:
            const, vola = False, False
            while peek() and peek()[1] in ("const", "vola"): #type:ignore
                kw = consume()[1]
                if kw == "const": const = True
                if kw == "vola": vola = True
            ton = consume("ID")[1]
            if ton in TYPEM:
                ftype = ton
                name = consume("ID")[1]
            else:
                ftype = None
                name = ton
            if peek() and peek()[0] == "ASSIGN": #type:ignore
                consume("ASSIGN")
                expr = parseexpr()
                if ftype is None: ftype = expr.type
            else:
                if ftype is None:
                    raise RuntimeError(f"variable '{name}' must have a type if no value is given")
                expr = None
            symbols[name] = {"type": ftype, "const": const}
            ast.append(VariableNode(name, expr, ftype, const, vola))
            
        # reassignment
        elif kind == "ID" and peek(1) and peek(1)[0] == "ASSIGN": #type:ignore
            name = consume("ID")[1]
            if name not in symbols:
                raise RuntimeError(f"variable 'name' not declared")
            if symbols[name]["const"]:
                raise RuntimeError(f"cannot reassign constant '{name}'")
            consume("ASSIGN")
            expr = parseexpr()
            if expr.type != symbols[name]["type"]:
                raise RuntimeError(f"type mismatch: cannot assign {expr.type} to {symbols[name]["type"]}")
            ast.append(AssignmentNode(name, expr))