class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        result=[]
        queue=collections.deque([root])
        while queue:
            level=[]
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                for child in cur.children:
                    queue.append(child)
            result.append(level)
        return result