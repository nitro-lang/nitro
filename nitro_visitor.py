class NitroVisitor():

    def process(self,tree):

        print(tree)

        if isinstance(tree[0],tuple):
            self.process(tree[0])

        else:
            match tree[0]:
                case "add":
                    return self.add(tree[1],tree[2])
                case "sub":
                    return self.sub(tree[1],tree[2])
                case "mul":
                    return self.mul(tree[1],tree[2])
                case "div":
                    return self.div(tree[1],tree[2])

    def add(self,left,right):
        if isinstance(left,tuple):
            left_value = self.process(left)
        else: left_value = left

        if isinstance(right,tuple):
            right_value = self.process(right)
        else: right_value = right

        return left_value + right_value
    
    def sub(self,left,right):
        if isinstance(left,tuple):
            left_value = self.process(left)
        else: left_value = left

        if isinstance(right,tuple):
            right_value = self.process(right)
        else: right_value = right

        return left_value - right_value
    
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

