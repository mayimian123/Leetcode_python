class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(node:TreeNode):
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    
## 中序遍历 递归写法


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        cur=root
        stack=[]
        while cur or stack:
            if cur is not None:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                res.append(cur.val)
                cur=cur.right
        return res
    
## 中序遍历 迭代写法