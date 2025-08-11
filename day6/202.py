class Solution:
    def isHappy(self, n: int) -> bool:
        record=set()
        while True:
            n=self.get_sum(n)
            if n in record:
                return False
            if n==1:
                return True
            else:
                record.add(n)

        return self.get_sum(n)
    def get_sum(self, n: int) -> int:
        res=0
        while n:
            n,r=divmod(n,10)
            res+=r**2
        return res