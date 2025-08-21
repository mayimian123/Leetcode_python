class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
    def getDepth(self, root) -> int:
        if root is None:
            return 0
        left_length=self.getDepth(root.left)
        right_length=self.getDepth(root.right)
        if root.right is None and root.left is not None:
            return 1+left_length
        if root.right is not None and root.left is None:
            return 1+right_length
        length=1+min(right_length,left_length)
        return length