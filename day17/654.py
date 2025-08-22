class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==1:
            return TreeNode(nums[0])
        node=TreeNode(0)
        max_value=0
        max_value_index=0
        for i in range(len(nums)):
            if nums[i]>max_value:
                max_value=nums[i]
                max_value_index=i
        node.val=max_value
        if max_value_index > 0: #左边还有位置
            new_list=nums[:max_value_index]
            node.left=self.constructMaximumBinaryTree(new_list)
        if max_value_index < len(nums)-1:
            new_list=nums[max_value_index+1:]
            node.right=self.constructMaximumBinaryTree(new_list)
        return node
