import time
from nitro_lexer import *
from nitro_parser import *
from nitro_visitor import *


if __name__ == "__main__":
    start = time.perf_counter()

    lexer = NitroLexer()
    parser = NitroParser()
    visitor = NitroVisitor()

    file = open("input.txt")
    code = file.read()

    tokens = lexer.tokenize(code)
    tree = parser.parse(tokens)
    print(visitor.process(tree))

    end = time.perf_counter()

    print(f"--- process took {end - start:0.4f} seconds ---")
