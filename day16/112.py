class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.traversal(root,targetSum - root.val)
    def traversal(self,cur:TreeNode,count:int)->bool:
        if not cur.left and not cur.right and count==0:
            return True
        if not cur.left and not cur.right:
            return False
        if cur.left:
            count-=cur.left.val
            if self.traversal(cur.left,count):
                return True
            count+=cur.left.val
        if cur.right:
            count-=cur.right.val
            if self.traversal(cur.right,count):
                return True
            count+=cur.right.val
        return False