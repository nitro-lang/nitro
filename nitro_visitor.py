from llvmlite import ir
import llvmlite.binding as binding


class NitroVisitor():

    def __init__(self,name):

        self.module = ir.Module(name)
        self.builder = None

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
                    return self.mul(tree[1],tree[2])
                case "div":
                    return self.div(tree[1],tree[2])
                case "func":
                    return self.func(tree[1],tree[2],tree[3])


    def add(self,builder,left,right):
        if isinstance(left,tuple):
            left_value = self.process(left)
        else: left_value = left

        if isinstance(right,tuple):
            right_value = self.process(right)
        else: right_value = right

        builder.add(ir.Constant(ir.IntType(32),left_value),ir.Constant(ir.IntType(32),right_value))
    
    def sub(self,builder,left,right):
        if isinstance(left,tuple):
            left_value = self.process(left)
        else: left_value = left

        if isinstance(right,tuple):
            right_value = self.process(right)
        else: right_value = right

        builder.sub(ir.Constant(ir.IntType(32),left_value),ir.Constant(ir.IntType(32),right_value))
    
    def mul(self,left,right):
        if isinstance(left,tuple):
            left_value = self.process(left)
        else: left_value = left

        if isinstance(right,tuple):
            right_value = self.process(right)
        else: right_value = right

        return left_value * right_value

    def div(self,left,right):
        if isinstance(left,tuple):
            left_value = self.process(left)
        else: left_value = left

        if isinstance(right,tuple):
            right_value = self.process(right)
        else: right_value = right

        return left_value / right_value
    
    def func(self,id,args,instructions):

        if isinstance(args,tuple):
            args_value = self.process(args)
        else: args_value = args

        return_type = ir.VoidType()
        function_type = ir.FunctionType(return_type,())
        function = ir.Function(self.module, function_type, name=id)

        block = function.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        
        for instruction in instructions:
            self.process(builder,instruction)

        builder.ret_void()





        

