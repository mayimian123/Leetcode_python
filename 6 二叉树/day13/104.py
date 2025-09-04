class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: #如果节点是空的 则说明深度为0
            return 0
        queue=collections.deque([root]) #存储root queue代表每一列
        result=0
        while queue:
            for _ in range(len(queue)):
                cur=queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result+=1 #层序一次的话结果就+1
        return result
#利用层序遍历来求二叉树的深度