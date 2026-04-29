import re

# cardea lexer
# made by las-r on github

class token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"token({self.type}, \"{self.value}\", {self.line}:{self.column})"

class lexer:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.rules = [
            ("comment",  r"#.*"),                    
            ("str",      r"\"[^\"]*\""),                
            ("flt",      r"\d+\.\d+"),               
            ("int",      r"\d+"),                    
            ("keyword",  r"\b(int|flt|str|bit|void|const|return|if|else|end|while|for|print|input|use)\b"),
            ("id",       r"[a-z][a-z0-9]*"),         
            ("op",       r"==|!=|>=|<=|[=+*/<>-]"),  
            ("sigil",    r"[@<>,()]"),               
            ("newline",  r"\n"),                     
            ("skip",     r"[ \t]+"),                 
            ("mismatch", r"."),                      
        ]
        self.regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in self.rules)

    def tokenize(self):
        linenum = 1
        linestart = 0
        for mo in re.finditer(self.regex, self.source):
            kind = mo.lastgroup
            value = mo.group()
            column = mo.start() - linestart
            if kind == "newline":
                linestart = mo.end()
                linenum += 1
            elif kind == "skip" or kind == "comment":
                continue
            elif kind == "mismatch":
                raise SyntaxError(f"unexpected character \"{value}\" at line {linenum}")
            else:
                self.tokens.append(token(kind, value, linenum, column))
        return self.tokens