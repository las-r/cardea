import os
import subprocess
import sys
from cardea.lexer import lexer
from cardea.parser import parser
from cardea.emitter import emitter

# cardea main
# made by las-r on github

def main():
    # parse args
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("usage: cardea <filename.car>")
        return

    # open file
    try:
        with open(filename) as file:
            source = file.read()
    except FileNotFoundError:
        print(f"file error: file {filename} not found")
        return

    # lex
    try:
        l = lexer(source)
        tokens = l.tokenize()
    except Exception as e:
        print(f"lexer error: {e}")
        return

    # parse
    try:
        p = parser(tokens)
        ast = p.parse()
    except Exception as e:
        print(f"parser error: {e}")
        return

    # emit
    try:
        e = emitter()
        ccode = e.emit(ast)
    except Exception as e:
        print(f"emitter error: {e}")
        return

    # build
    if not os.path.exists("carbuild"):
        os.makedirs("carbuild")
    with open("carbuild/out.c", "w") as f:
        f.write(ccode)
    try:
        subprocess.run(["gcc", "carbuild/out.c", "-o", "carbuild/out"], check=True)
        print("build successful!")
    except FileNotFoundError:
        print("build error: gcc not found. please install mingw or w64devkit.")
    except subprocess.CalledProcessError:
        print("build error: gcc found but failed to compile the code.")
        
if __name__ == "__main__":
    main()