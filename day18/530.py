class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.vec=[]
        self.travelsal(root)
        if len(self.vec)<=1:
            return 0
        result=float('inf')
        for i in range(1,len(self.vec)):
            result=min(result,self.vec[i]-self.vec[i-1])
        return result
    def __init__(self):
        self.vec=[]
    def travelsal(self,root):
        if root is None:
            return
        self.travelsal(root.left)
        self.vec.append(root.val)
        self.travelsal(root.right)