class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue=collections.deque([root])
        while queue:
            levelsize=len(queue)
            for _ in range(len(queue)):
                cur=queue.popleft()
                if _==levelsize-1:
                    cur.next=None
                else:
                    cur.next=queue[0]
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root