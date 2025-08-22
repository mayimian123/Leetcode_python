class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        leftValue = self.sumOfLeftLeaves(root.left)
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftValue=root.left.val
        rightValue = self.sumOfLeftLeaves(root.right)
        sumval=leftValue+rightValue
        return sumval
# 注意左叶子的定义 rightvalue代表的是进入右子树来递归