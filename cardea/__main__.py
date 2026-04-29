import os
import subprocess
import sys
from cardea.lexer import lexer
from cardea.parser import parser
from cardea.emitter import emitter

def main():
    # parse args
    if len(sys.argv) >= 1:
        filename = sys.argv[1]
    else:
        print("usage: cardea <filename.car>")
        return

    # open file
    try:
        with open(filename) as file:
            source = file.read()
    except FileNotFoundError:
        print(f"error: file '{filename}' not found")
        return

    # lex
    l = lexer(source)
    tokens = l.tokenize()

    # parse
    p = parser(tokens)
    ast = p.parse()

    # emit
    e = emitter()
    ccode = e.emit(ast)

    # build
    if not os.path.exists("carbuild"):
        os.makedirs("carbuild")
    with open("carbuild/out.c", "w") as f:
        f.write(ccode)
    try:
        subprocess.run(["gcc", "build/out.c", "-o", "build/out"], check=True)
        print("compilation successful!")
    except FileNotFoundError:
        print("error: gcc not found. please install mingw or w64devkit.")
    except subprocess.CalledProcessError:
        print("error: gcc found but failed to compile the code.")
        
if __name__ == "__main__":
    main()