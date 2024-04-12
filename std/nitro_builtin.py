from llvmlite import ir

is_builtin_setup = {
    "print" : False
}

def c_print(builder : ir.IRBuilder,module,string):

    voidptr_ty = ir.IntType(8).as_pointer()

    global printf

    if is_builtin_setup["print"] == False:

        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(module, printf_ty, name="printf")

        is_builtin_setup["print"] = True

    c_str_val = ir.Constant(ir.ArrayType(ir.IntType(8), len(string)),bytearray(string.encode("utf8")))
    c_str = builder.alloca(c_str_val.type)
    builder.store(c_str_val, c_str)
    fmt_arg = builder.bitcast(c_str, voidptr_ty)
    builder.call(printf, [fmt_arg])

builtin_functions = {
    "print" : c_print
}

