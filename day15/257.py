class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        path=[]
        if root is None:
            return result
        self.traversal(root,path,result)
        return result
    def traversal(self,cur,path,result):
        path.append(cur.val)
        if cur.left is None and cur.right is None:
            sPath='->'.join(map(str,path))
            result.append(sPath)
            return
        if cur.left:
            self.traversal(cur.left,path,result)
            path.pop()
        if cur.right:
            self.traversal(cur.right,path,result)
            path.pop()