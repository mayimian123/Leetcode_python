class MyQueue:

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self) -> int:
        if self.empty():
            return None
        if self.stack_out==[]:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
    
    def empty(self) -> bool:
        if self.stack_out==[] and self.stack_in==[]:
            return True
        else:
            return False

## 用两个栈来实现队列
## 核心是pop的时候如果没有元素需要把push的全部都导入进去
## 写条件的时候尽量写全以免混淆