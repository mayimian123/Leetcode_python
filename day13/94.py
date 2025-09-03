class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]#存储结果
        def dfs(node:TreeNode):
            if node is None: # 递归出口
                return
            dfs(node.left)   # 递归逻辑
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    
## 中序遍历 递归写法
## 返回二叉树的中序遍历结果

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        cur=root
        stack=[] #调用栈
        while cur or stack:
            if cur is not None:#不断获取左边的元素
                stack.append(cur)
                cur=cur.left
            else:#如果左边没有元素了 退回当前的值 并且如果有右子树 则去处理右子树
                cur=stack.pop()
                res.append(cur.val)
                cur=cur.right
        return res
    
## 中序遍历 迭代写法
## 迭代和递归的区别
## 迭代是不断重复相同的动作直到完成最终的结果
## 递归是将大的问题拆分为小的问题 然后不断重复完成最终的结果