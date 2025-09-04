class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p=0
        while p<len(s):
            p2=p+k
            s=s[:p]+s[p:p2][::-1]+s[p2:]
            p=p+2*k
        return s
    

## 也是采用指针的方法
## 核心部分link6 是使用str拼接 其中[::-1]是反转的