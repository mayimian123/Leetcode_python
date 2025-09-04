class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res=[]
        def dfs(node:TreeNode):
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        print(res)
        for i in range(len(res)):
            if res[i]!=res[-i-1]:
                return False
        return True
## 解法 这个只AC了195/200 因为
#     1
#    / \
#   2   2
#    \   \
#     3   3
# 中序遍历结果：[2, 3, 1, 2, 3]
# 对称吗？表面上看“差不多”，但实际树结构是不对称的。
# 所以不能用中序序列直接判断对称。

#只能变为递归的方法去解答

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left:TreeNode,right:TreeNode):
            if not left and right: return False
            elif not left and not right: return True
            elif left and not right: return False
            elif left.val != right.val: return False
            
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        if root==None:
            return True
        return dfs(root.left,root.right)