from operator import add, sub, mul
def div(a:int,b:int)->int:
    return int(a/b) if a*b>0 else -(abs(a)//abs(b))

class Solution:
    op_map={'+':add,'-':sub,'*':mul,'/':div}
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for token in tokens:
            if token not in{'+','-','*','/'}:
                stack.append(int(token))
            else:
                a=stack.pop()
                b=stack.pop()
                stack.append(self.op_map[token](b,a))
        return stack.pop()