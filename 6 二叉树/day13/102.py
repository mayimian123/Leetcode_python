class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:  #如果节点为空 返回空
            return []
        queue=collections.deque([root]) #用来存储每一行的节点 变为队列 一开始的话只存root
        result=[]
        while queue:    #一直到遍历所有的节点
            level=[]    #代表每一层的结果
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result
# 层序遍历levelorder