class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq_map = defaultdict(int)
        result = []
        if root is None:
            return result
        self.searchBST(root,freq_map)
        max_freq=max(freq_map.values())
        for key,freq in freq_map.items():
            if freq == max_freq:
                result.append(key)
        return result
    def searchBST(self,cur,freq_map):
        if cur is None:
            return
        freq_map[cur.val]+=1
        self.searchBST(cur.left,freq_map)
        self.searchBST(cur.right,freq_map)