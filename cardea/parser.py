from .nodes import *

# cardea parser
# made by las-r on github

class parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # helpers
    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    def consume(self, expectedtype=None):
        token = self.peek()
        if not token or (expectedtype and token.type != expectedtype):
            posinfo = f"{token.line}:{token.column}" if token else "EOF"
            raise Exception(f"Expected {expectedtype} at {posinfo}")
        self.pos += 1
        return token

    # expression parser
    def parseexpr(self):
        token = self.peek()
        if token.type in ["str", "int", "flt"]:#type:ignore
            t = self.consume()
            return literalnode(t.type, t.value)
        if token.type == "id":#type:ignore
            t = self.consume()
            return variablenode(t.value)
        raise Exception(f"invalid expression: {token.value}")#type:ignore

    # statement parser
    def parsestatement(self):
        token = self.peek()
        
        # literal
        if token.type in ["str", "int", "flt", "bit"]:#type:ignore
            t = self.consume()
            return literalnode(t.type, t.value)
        
        # print
        if token.type == "keyword" and token.value == "print":#type:ignore
            self.consume()
            expr = self.parseexpr() 
            return printnode(expr)
        
        return None

    # full parser
    def parse(self):
        body = []
        while self.peek():
            stmt = self.parsestatement()
            if stmt:
                body.append(stmt)
            else:
                raise Exception(f"unexpected token: {self.peek().value}")#type:ignore
        return filenode(body)