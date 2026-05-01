# cardea nodes
# made by las-r on github

# filebody node
class filenode:
    def __init__(self, body):
        self.body = body
        
# value nodes
class literalnode:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

class variableassignnode:
    def __init__(self, type_, name, value):
        self.type = type_
        self.name = name
        self.value = value

class variablenode:
    def __init__(self, name):
        self.name = name

# builtin op nodes
class printnode:
    def __init__(self, value):
        self.value = value