from nitro_lexer import *
from nitro_parser import *
from nitro_visitor import *
import time
import argparse


if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file", help="The main file of program to be compiled", type=str)

    args = arg_parser.parse_args()

    start = time.perf_counter()

    try:

        file = open(args.file)
        code = file.read()

    except:
        print(f"File \'{args.file}\' not found")

    else:

        lexer = NitroLexer()
        parser = NitroParser()
        visitor = NitroVisitor()

        tokens = lexer.tokenize(code)
        parser.parse(tokens)

        for instruction in instructions:
            print(visitor.process(instruction))

        end = time.perf_counter()

        print(f"--- process took {end - start:0.4f} seconds ---")
