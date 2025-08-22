class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None #如果序列为空 那么没有节点 返回None
        root_val=postorder[-1]
        root = TreeNode(postorder[-1]) # 前序遍历的第一个节点就是根节点
        separator_idx = inorder.index(root_val) # 在中序遍历中找到
        inorder_left=inorder[:separator_idx]
        inorder_right=inorder[separator_idx+1:]
        postorder_left=postorder[:len(inorder_left)]
        postorder_right=postorder[len(inorder_left):len(postorder)-1]
        root.left = self.buildTree(inorder_left,postorder_left)
        root.right=self.buildTree(inorder_right,postorder_right)
        return root