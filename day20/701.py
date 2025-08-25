class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root=TreeNode(val)
            return root
        if val<root.val:#向左走 左小右大
            root.left=self.insertIntoBST(root.left,val)
        if val>root.val:
            root.right=self.insertIntoBST(root.right,val)
        return root