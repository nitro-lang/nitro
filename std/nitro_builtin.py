from llvmlite import ir

types = {
    "void" : ir.VoidType(),
    "int4" : ir.IntType(4),
    "int8" : ir.IntType(8),
    "int16" : ir.IntType(16),
    "int32" : ir.IntType(32),
    "int64" : ir.IntType(64),
    "half" : ir.HalfType(),
    "double" : ir.DoubleType(),
    "float" : ir.FloatType()
}

def bitcast(builder: ir.IRBuilder,value,type):
    return builder.bitcast(value,type)

is_builtin_setup = {
    "print" : False
}

def c_print(builder : ir.IRBuilder,module,args):

    voidptr_ty = ir.IntType(8).as_pointer()

    global printf

    if is_builtin_setup["print"] == False:

        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(module, printf_ty, name="printf")

        is_builtin_setup["print"] = True

    fmt = []

    for arg in args:
        if isinstance(arg,str):
            fstr = ir.Constant(ir.ArrayType(ir.IntType(8), len(arg)),bytearray(arg.encode("utf8")))
            c_str = builder.alloca(fstr.type)
            builder.store(fstr, c_str)
            fmt.append(builder.bitcast(c_str, voidptr_ty))
        elif isinstance(arg,int):
            fmt.append(ir.Constant(ir.IntType(8),arg))
        elif isinstance(arg,ir.AllocaInstr):
            value = bitcast(builder,arg,ir.IntType(32).as_pointer())
            fmt.append(builder.load(value))
        else:        
            fmt.append(bitcast(builder,arg,ir.IntType(32)))

    builder.call(printf, fmt)

def write_reg(builder : ir.IRBuilder,module,arg):

    builder.store_reg(arg[0],arg[1],arg[2].replace("\0",""))

def read_reg(builder : ir.IRBuilder,module,arg):
    return builder.load_reg(arg[0],arg[1].replace("\0",""))

builtin_functions = {
    "print" : c_print,
    "write_reg" : write_reg,
    "read_reg" : read_reg
}

