class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        result=[]
        queue=collections.deque([root])
        while queue:
            levelsize=len(queue)
            levelsum=0
            for i in range(levelsize):
                cur=queue.popleft()
                levelsum=levelsum+cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(levelsum/levelsize)
        return result