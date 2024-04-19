from llvmlite import ir
from llvmlite import binding
from std.nitro_builtin import *

class NitroVisitor():

    def __init__(self,name):

        self.module = ir.Module(name)
        self.builder = None
        self.functions = {}
        self.function_vars = {}

    def process(self,builder,tree):

        if isinstance(tree[0],tuple):
            return self.process(tree[0])

        else:
            match tree[0]:
                case "add":
                    return self.add(builder,tree[1],tree[2])
                case "sub":
                    return self.sub(builder,tree[1],tree[2])
                case "mul":
                    return self.mul(builder,tree[1],tree[2])
                case "div":
                    return self.div(builder,tree[1],tree[2])
                case "var":
                    return self.var(builder,tree[1],tree[2],tree[3])
                case "func":
                    return self.func(tree[1],tree[2],tree[3])
                case "call":
                    return self.call(builder,tree[1],tree[2])
                case "arg":
                    return self.arg(builder,tree[1])
                case "get":
                    return self.get(builder,tree[1])


    def add(self,builder : ir.IRBuilder,left,right):
        if isinstance(left,tuple):
            left_value = self.process(builder,left)
        else: left_value = ir.Constant(ir.IntType(32),left)

        if isinstance(right,tuple):
            right_value = self.process(builder,right)
        else: right_value = ir.Constant(ir.IntType(32),right)

        return builder.add(left_value,right_value)
    
    def sub(self,builder,left,right):
        if isinstance(left,tuple):
            left_value = self.process(builder,left)
        else: left_value = ir.Constant(ir.IntType(32),left)

        if isinstance(right,tuple):
            right_value = self.process(builder,right)
        else: right_value = ir.Constant(ir.IntType(32),right)

        return builder.sub(ir.Constant(ir.IntType(32),left_value),ir.Constant(ir.IntType(32),right_value))
    
    def mul(self,builder : ir.IRBuilder,left,right):
        if isinstance(left,tuple):
            left_value = self.process(builder,left)
        else: left_value = ir.Constant(ir.IntType(32),left)

        if isinstance(right,tuple):
            right_value = self.process(builder,right)
        else: right_value = ir.Constant(ir.IntType(32),right)

        return builder.mul(left_value,right_value)

    def div(self,builder,left,right):
        if isinstance(left,tuple):
            left_value = self.process(builder,left)
        else: left_value = ir.Constant(ir.IntType(32),left)

        if isinstance(right,tuple):
            right_value = self.process(builder,right)
        else: right_value = ir.Constant(ir.IntType(32),right)

        return builder.div(left_value,right_value)
    
    def var(self,builder : ir.IRBuilder,name,value,type):
        if type == None:
            type = types["null"]
        else: type = types[type]
        
        ptr = builder.alloca(type,None,name)

        if isinstance(value,tuple):
            value = self.process(builder,value)
            builder.store(value,ptr)
        else: 
            builder.store(ir.Constant(type,value),ptr)

        
        self.function_vars[name] = ptr

    def func(self,id,args,instructions):

        if isinstance(args,tuple):
            args_value = self.process(args)
        else: args_value = args

        return_type = ir.VoidType()
        function_type = ir.FunctionType(return_type,())
        function = ir.Function(self.module, function_type, name=id)

        self.functions[id] = function

        block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        
        for instruction in instructions:
            self.process(builder,instruction)

        builder.ret_void()

    def call(self,builder : ir.IRBuilder,id,args):

        args_list = []

        for arg in args:

            arg = self.process(builder,arg)              
            args_list.append(arg)
            
        if id in builtin_functions:
            return builtin_functions[id](builder,self.module,args_list)

        else:
            return builder.call(self.functions[id], args)

    def arg(self,builder,arg):

        if isinstance(arg,tuple):
            return self.process(builder,arg) 
        else: return arg
        
    def get(self,builder : ir.IRBuilder,name):

        if name in types:
            return types[name]
        return builder.load(self.function_vars[name])
        
         

