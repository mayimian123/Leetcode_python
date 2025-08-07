class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minl = float('inf')
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                minl = min(minl, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        return 0 if minl == float('inf') else minl