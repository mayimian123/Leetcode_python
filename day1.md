## Day1 Info
- Topic: Array
- Language:python
- https://programmercarl.com/%E6%95%B0%E7%BB%84%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html
---
## 704 Binary Search
### Thought
1. Brute Force solution 没有什么难度
```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i==target:
                return nums.index(i)
        return -1
```
2. 二分法binary search 左闭右闭 时间复杂度：O(log n) 空间复杂度：O(1)
```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2 
            if target==nums[mid]:
                return mid
            elif target < nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1
```

### Link
704. 二分查找 
题目建议： 大家今天能把 704.二分查找 彻底掌握就可以，至于 35.搜索插入位置 和 34. 在排序数组中查找元素的第一个和最后一个位置 ，如果有时间就去看一下，没时间可以先不看，二刷的时候在看。
先把 704写熟练，要熟悉 根据 左闭右开，左闭右闭 两种区间规则 写出来的二分法。
题目链接：https://leetcode.cn/problems/binary-search/
文章讲解：https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html
视频讲解：https://www.bilibili.com/video/BV1fA4y1o715

---
## 27 移除元素 Remove Element
### Thought
1. 新建一个数组 直接append-> 不符合原地修改的要求（in-place） In computer science, an in-place algorithm is an algorithm that operates directly on the input data structure without requiring extra space proportional to the input size. 

2. 快慢指针 虽然看起来叫做快慢指针 但是本质上就是直接筛选合适的向前覆盖 时间复杂度O(n) 空间复杂度O(1) 
```Python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for i in nums:
            if i!=val:
                nums[j]=i
                j+=1
        return j
```

### Link
题目建议：  暴力的解法，可以锻炼一下我们的代码实现能力，建议先把暴力写法写一遍。 双指针法 是本题的精髓，今日需要掌握，至于拓展题目可以先不看。 
题目链接：https://leetcode.cn/problems/remove-element/ 
文章讲解：https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html
视频讲解：https://www.bilibili.com/video/BV12A4y1Z7LP 

---

## 977 有序数组的平方 
### Thought
1. 暴力方法 先平方后面再sort
```Python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(nums):
            nums[i]=nums[i]**2
        nums.sort()
        return nums
```
2. 双指针方法 顺序是一个难点
```Python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        size=len(nums)-1
        new=[0]*len(nums)
        while left<=right:
            if nums[left]**2<nums[right]**2:
                new[size]=nums[right]**2
                right-=1
            elif nums[left]**2>=nums[right]**2:
                new[size]=nums[left]**2
                left+=1
            size-=1
        return new
```
### Link
题目建议： 本题关键在于理解双指针思想 
题目链接：https://leetcode.cn/problems/squares-of-a-sorted-array/
文章讲解：https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html
视频讲解： https://www.bilibili.com/video/BV1QB4y1D7ep 

---

### Harvest
- [x] be more familiar with markdown
- [x] learn how to use git and github more familiar
- [x] successfully download leetcode extension in vscode!! which is sooo convient!! Don't forget confirm email to access all available features
- [x] can not add condition after "else"