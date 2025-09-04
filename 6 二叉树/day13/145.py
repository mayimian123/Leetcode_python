class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(node:TreeNode):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
## 后序遍历 递归方法


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        stack=[root]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return res[::-1]
## 后序遍历 迭代方法 左右中 等价于直接中右左的[::-1]