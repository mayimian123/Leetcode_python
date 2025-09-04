class MyStack:

    def __init__(self):
        self.quene=deque()

    def push(self, x: int) -> None:
        self.quene.append(x)

    def pop(self) -> int:
        if self.empty()==True:
            return None
        for i in range(len(self.quene)-1):
            self.quene.append(self.quene.popleft())
        return self.quene.popleft()

    def top(self) -> int:
        if self.empty()==True:
            return None
        return self.quene[-1]

    def empty(self) -> bool:
        return not self.quene
    
## 用队列模拟栈 deque-> double end quene
## return not self.quene 当quene有东西为true 这里的not是取反
## pop的逻辑是希望将除了目标的元素都向右