## Method 1: use dict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records=dict()
        for index,value in enumerate(nums):
            if target-value in records:
                return[records[target-value],index]
            records[value]=index
        return []
# enumerate 枚举

## Method 2: use set
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records=set()
        for i,num in enumerate(nums):
            if target-num in records:
                return[i,nums.index(target-num)]
            records.add(num)
        return []