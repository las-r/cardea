from .nodes import *

# cardea parser
# made by las-r on github

class parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expectedtype):
        token = self.peek()
        if not token or token.type != expectedtype:
            raise Exception(f"expected {expectedtype}")
        self.pos += 1
        return token

    def parse(self):
        body = []
        while self.peek():
            if self.peek().type == "keyword" and self.peek().value == "print": #type:ignore
                self.consume("keyword")
                val = self.consume("str")
                body.append(printnode(val.value))
        return filenode(body)