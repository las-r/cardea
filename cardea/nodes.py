# cardea nodes
# made by las-r on github

# node class
class node:
    def __init__(self):
        pass

# file nodes
class filenode(node):
    def __init__(self, body):
        self.body = body

# builtin op nodes
class printnode(node):
    def __init__(self, value):
        self.value = value