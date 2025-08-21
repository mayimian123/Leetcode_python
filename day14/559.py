#n叉树的最大深度
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        max_depth=1
        for child in root.children:
            max_depth=max(max_depth,self.maxDepth(child)+1)
        return max_depth
#递归逻辑
# 对于非空节点，初始时候节点的深度为1
# 遍历当前的所有子节点，得到子树的深度 再加上1 因为节点到节点有一层距离
# 记录当前最大的深度和所有子树的深度 取最大值