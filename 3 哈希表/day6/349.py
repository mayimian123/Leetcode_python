# method1: use array
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index1=[0]*1001
        index2=[0]*1001
        result=[]
        for i in nums1:
            index1[i]=1
        for i in nums2:
            index2[i]=1
        for i in range(0,1001):
            if index1[i]==1 and index2[i]==1:
                result.append(i)
        return result
    
# method2: use set and dict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table={} #dictionary
        for i in nums1:
            table[i]=table.get(i,0)+1
        result=set()

        for i in nums2:
            if i in table:
                result.add(i)
                del table[i]

        return list(result) #need list()