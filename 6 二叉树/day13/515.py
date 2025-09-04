class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result=[]
        queue=collections.deque([root])
        while queue:
            maxnum=None
            for _ in range(len(queue)):
                cur=queue.popleft()
                if maxnum==None:
                    maxnum=cur.val
                else:
                    maxnum=max(maxnum,cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(maxnum)
        return result