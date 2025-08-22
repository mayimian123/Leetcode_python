class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth=float('-inf')
        self.result=None
        self.travelsal(root,0)
        return self.result
    def travelsal(self,node,depth):
        if not node.left and not node.right:
            if depth > self.max_depth: 
                self.max_depth = depth
                self.result = node.val
            return
        if node.left:
            depth+=1
            self.travelsal(node.left,depth)
            depth-=1
        if node.right:
            depth+=1
            self.travelsal(node.right,depth)
            depth-=1