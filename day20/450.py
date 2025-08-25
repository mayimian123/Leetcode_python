class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                cur=root.right
                while cur.left is not None:
                    cur=cur.left
                cur.left=root.left
                return root.right
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        return root