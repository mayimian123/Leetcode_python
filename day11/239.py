from typing import List, Deque
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list=[]
        kept_nums=deque()
        for i in range(len(nums)):
            update_kept_nums(kept_nums,nums[i])
            if i>=k and nums[i-k]==kept_nums[0]:
                kept_nums.popleft()
            if i>=k-1:
                max_list.append(kept_nums[0])
        return max_list
    
def update_kept_nums(kept_nums:deque[int],num:int):
    while kept_nums and num>kept_nums[-1]:
        kept_nums.pop()
    kept_nums.append(num)

## 感觉可以再做一遍
## 用kept_nums来作为存储的窗口 含义是一个单调递减的小窗口 只允许存在左边的值比右边的大 如果左边的值比右边的小那就都会pop出去
## 如果窗口超出长度了 或者是刚进入的值和kept_nums的最大值保持一致
    ## 那么就把最左边的元素给pop出去 用popleft
## 因为从k-1开始就需要不断的记录最大值了 所以就是if i>=k-1的每一次 都需要append存储数组里的第一个元素进去