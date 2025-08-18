class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue=collections.deque([root])
        result=0
        while queue:
            for _ in range(len(queue)):
                cur=queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result+=1
        return result
