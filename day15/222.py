class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.getNodesNum(root)
    def getNodesNum(self,cur):
        if cur is None:
            return 0
        leftNum=self.getNodesNum(cur.left)
        rightNum=self.getNodesNum(cur.right)
        treeNum=1+leftNum+rightNum
        return treeNum