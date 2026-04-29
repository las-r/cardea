# cardea types
# made by las-r on github

class type:
    def __init__(self, name, size=None, ispointer=False):
        self.name = name
        self.size = size
        self.ispointer = ispointer

    def __eq__(self, other):
        if not isinstance(other, type):
            return False
        return self.name == other.name and self.size == other.size