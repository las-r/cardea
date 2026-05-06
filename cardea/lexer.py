import re

# cardea lexer
# made by las-r on github

# token specifications
TOKENSPEC = [
    ('COMMENT',   r'#.*'),
    ('FLOATLIT', r'\d+\.\d+'),
    ('INTLIT',   r'\d+'),
    ('STRLIT',   r'"[^"]*"'),
    ('ASSIGN',    r'='),
    ('COLON',     r':'),
    ('COMMA',     r','),
    ('ID',        r'[a-zA-Z_]\w*'),
    ('NEWLINE',   r'\n'),
    ('SKIP',      r'[ \t]+'),
    ('MISMATCH',  r'.'),
]

# master regex
MASTER = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENSPEC)

# lexer
def lex(source):
    tokens = []
    lnum = 1
    lstart = 0
    for mo in re.finditer(MASTER, source):
        kind = mo.lastgroup
        value = mo.group()
        col = mo.start() - lstart #type:ignore
        if kind == "SKIP" or kind == "COMMENT":
            continue
        elif kind == "NEWLINE":
            lstart = mo.end
            lnum += 1
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"unexpected character {value!r} at {lnum}:{col}")
        tokens.append((kind, value, lnum, col))
    return tokens