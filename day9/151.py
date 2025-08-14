class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        w=w[::-1]
        return ' '.join(w)
    
## split()是分割任意空白字符
## w[::-1]反转字符
## ' '.join()用空格连接起来