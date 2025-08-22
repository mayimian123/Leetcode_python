class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.vec = []
        self.traversal(root)
        for i in range(1,len(self.vec)):
            if self.vec[i]<=self.vec[i-1]:
                return False
        return True
    def traversal(self, root):
        if root is None:
            return 
        self.traversal(root.left)
        self.vec.append(root.val)
        self.traversal(root.right)
        
    def __init__(self):
        self.vec=[]