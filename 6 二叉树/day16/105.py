class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val=preorder[0]
        root=TreeNode(root_val)
        spr_idx=inorder.index(root_val)
        inorder_left=inorder[:spr_idx]
        inorder_right=inorder[spr_idx+1:]
        preorder_left=preorder[1:1+len(inorder_left)]
        preorder_right=preorder[1+len(inorder_left):]
        root.left=self.buildTree(preorder_left,inorder_left)
        root.right=self.buildTree(preorder_right,inorder_right)
        
        return root