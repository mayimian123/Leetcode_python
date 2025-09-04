class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == q or root ==p or root is None:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left is not None and right is not None:
            return root
        if left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left
        else:
            return None
        
        ##需要二刷理解