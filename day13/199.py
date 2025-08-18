class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result=[]
        queue=collections.deque([root])
        while queue:
            for i in range(len(queue)):
                cur=queue.popleft()
                if i==0:
                    result.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        return result
    
##二叉树的右视图 只看右边的节点