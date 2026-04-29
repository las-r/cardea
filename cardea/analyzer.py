# cardea analyzer
# made by las-r on github

class analyzer:
    def __init__(self):
        self.scope = {}

    def analyze(self, node):
        methodname = "visit" + node.__class__.__name__
        visitor = getattr(self, methodname, self.genericvisit)
        return visitor(node)

    def genericvisit(self, node):
        raise Exception(f"no visit method for {node.__class__.__name__}")

    def visitfilenode(self, node):
        for stmt in node.body:
            self.analyze(stmt)

    def visitliteralnode(self, node):
        return node.type

    def visitvarassignnode(self, node):
        valuetype = self.analyze(node.value)
        
        if node.typehint:
            if node.typehint != valuetype:
                raise Exception(f"type mismatch for {node.name}")
        
        node.inferredtype = valuetype
        self.scope[node.name] = valuetype

    def visitbinopnode(self, node):
        lefttype = self.analyze(node.left)
        righttype = self.analyze(node.right)

        if lefttype != righttype:
            raise Exception(f"cannot perform {node.op} on {lefttype} and {righttype}")
        
        node.inferredtype = lefttype
        return lefttype