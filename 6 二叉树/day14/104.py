class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getdepth(root)
    def getdepth(self,node)->int:
        if node is None:
            return 0
        lefth=self.getdepth(node.left)
        righth=self.getdepth(node.right)
        length=1+max(lefth,righth)
        return length
#递归方法 相信递归的力量hhh！