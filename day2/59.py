class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for _ in range(n)]
        i=0
        diff=0
        j=n-1-diff
        count=1
        while diff<=n//2-1:
            i=diff
            for j in range(diff,n-1-diff):
                res[i][j]=count
                count+=1
            j=n-1-diff
            for i in range(diff,n-1-diff):
                res[i][j]=count
                count+=1
            i=n-1-diff
            for j in range(n-1-diff,diff,-1):
                res[i][j]=count
                count+=1
            j=diff
            for i in range(n-1-diff,diff,-1):
                res[i][j]=count
                count+=1
            diff+=1
        if n % 2 == 1:
            res[n // 2][n // 2] = count
        return res
# 找规律 n为单数的时候需要手动把中间的一个格子给补充上去