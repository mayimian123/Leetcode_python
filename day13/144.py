class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dbs(node):
            if node is None:
                return
            res.append(node.val)
            dbs(node.left)
            dbs(node.right)
        dbs(root)
        return res
#前序遍历 递归方法


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        stack=[root]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
#前序遍历 迭代方法
