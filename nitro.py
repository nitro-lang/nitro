from nitro_globals import *
from nitro_lexer import *
from nitro_parser import *
from nitro_visitor import *
import time
import argparse


if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file", help="The main file of program to be compiled", type=str)
    arg_parser.add_argument("-o", help="Write output program to a file", type=str)
    arg_parser.add_argument("-optim", help="Optimize the output program",action="store_true", required=False)

    args = arg_parser.parse_args()

    start = time.perf_counter()

    try:
        file = open(args.file)
        code = file.read()

    except:
        print(f"{error_color}ERROR{reset_color} : File \'{args.file}\' not found")

    else:

        if code != "":
            lexer = NitroLexer()
            parser = NitroParser()
            visitor = NitroVisitor(args.file)
         
            tokens = lexer.tokenize(code)
            instructions = parser.parse(tokens)

            if instructions == None:
                raise SystemExit(f"{error_color}ERROR{reset_color} : No statement found")

            for instruction in instructions:
                visitor.process(None, instruction)

            if args.optim:
                module_ref = binding.parse_assembly(str(visitor.module))
                optim = binding.create_module_pass_manager()
                if optim.run(module=module_ref):
                    print(f"{info_color}INFO{reset_color} : Program is optimized")
                else:
                    print(f"{info_color}INFO{reset_color} : Program is already optimized")
                   

            end = time.perf_counter()

            print(f"--- process took {end - start:0.4f} seconds ---")

            if args.o == None:
                output = "out"

            else: output = args.o

            open(f"{output}.o","w").write(str(visitor.module))
            print(f"{success_color}SUCCESS{reset_color} : Program is written to \"{output}.o\"")

            visitor.module

        else:
            print(f"File \'{args.file}\' is empty")
