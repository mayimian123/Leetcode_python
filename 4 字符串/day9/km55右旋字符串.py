class Solution:
    def rightchange(self, n: int, s:str)->str:
        result=[]
        for i in range(len(s)-n,len(s)):
            result.append(s[i])
        for i in range(0,len(s)-n):
            result.append(s[i])
        return ''.join(result)

if __name__ == "__main__":
    n = int(input())
    s = input()
    
    obj = Solution()
    result = obj.rightchange(n, s)
    print(result)