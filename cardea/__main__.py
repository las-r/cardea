import os
import subprocess
import sys
from .lexer import lex
from .parser import parse
from .emitter import emit

# cardea main
# made by las-r on github

def main():
    if len(sys.argv) < 2:
        print("usage: cardea <filename.car>")
        return
    
    # load source
    try:
        sourcepath = sys.argv[1]
        with open(sourcepath) as f:
            source = f.read()
    except Exception as e:
        print(f"source error: {e}")
        return
        
    # lex
    try:
        tokens = lex(source)
    except Exception as e:
        print(f"lexer error: {e}")
        return
    
    # parse
    try:
        ast = parse(tokens)
    except Exception as e:
        print(f"parser error: {e}")
        return
    
    # emit
    try:
        ccode = emit(ast)
    except Exception as e:
        print(f"emitter error: {e}")
        return
        
    # build
    if not os.path.exists("cbuild"):
        os.makedirs("cbuild")
    with open("cbuild/out.c", "w") as f:
        f.write(ccode)
    try:
        subprocess.run(["gcc", "cbuild/out.c", "-o", "cbuild/out"], check=True)
        print(f"successfully built!")
    except FileNotFoundError:
        print("build error: gcc not found")
    except subprocess.CalledProcessError:
        print("build error: gcc found but compilation failed")

if __name__ == "__main__":
    main()