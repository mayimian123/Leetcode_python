class Solution:# 二叉搜索树 左小右大
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.travelsal(root, p, q)
    def travelsal(self, cur, p, q):
        if cur is None:
            return cur
        if cur.val > p.val and cur.val > q.val:
            left=self.travelsal(cur.left,p,q)
            if left is not None:
                return left
        if cur.val < p.val and cur.val < q.val:
            right=self.travelsal(cur.right,p,q)
            if right is not None:
                return right
        return cur
