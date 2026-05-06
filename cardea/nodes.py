# cardea nodes
# made by las-r on github

# constants
TYPEM = {
    "int64": "int64_t",
    "int32": "int32_t",
    "int16": "int16_t",
    "int8": "int8_t",
    "uint64": "uint64_t",
    "uint32": "uint32_t",
    "uint16": "uint16_t",
    "uint8": "uint8_t",
    "float16": "_Float16",
    "float32": "float",
    "float64": "double",
    "bool": "bool",
    "char": "char",
    "str": "str",
    "void": "void",
}

FORMATM = {
    "int64": '" %" PRId64 "',
    "int32": '" %" PRId32 "',
    "int16": '" %" PRId16 "',
    "int8":  '" %" PRId8 "',
    "uint64": '" %" PRIu64 "',
    "uint32": '" %" PRIu32 "',
    "uint16": '" %" PRIu16 "',
    "uint8":  '" %" PRIu8 "',
    "float16": '" %f "',
    "float32": '" %f "',
    "float64": '" %lf "', 
    "float128": '" %Qg "',
    "bool": '" %d "',
    "char": '" %c "',
    "str":  '" %s "',
}


# keyword nodes
class PrintNode:
    def __init__(self, expr, newline=True):
        self.expr = expr
        self.newline = newline
    
    def emit(self, context):
        val = self.expr.emit(context)
        typ = TYPEM[self.expr.type]
        fmt = FORMATM[typ].strip('" ')
        nl = "\\n" if self.newline else ""
        return f'printf("{fmt}{nl}", {val})'
        
class InputNode:
    def __init__(self, target):
        self.target = target
        
# value nodes
class LiteralNode:
    def __init__(self, value, type_):
        self.value = value
        self.type = type_
    
    def emit(self, context):
        return self.value
        
class VariableNode:
    def __init__(self, name, expr, type_, const=False, vola=False):
        self.name = name
        self.expr = expr
        self.type = type_
        self.const = const
        self.vola = vola
        
class VariableRefNode:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_
        
class AssignmentNode:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr