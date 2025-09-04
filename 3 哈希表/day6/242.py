class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        index=[0]*26
        for i in s:
            index[ord(i)-ord('a')]+=1
        for i in t:
            index[ord(i)-ord('a')]-=1
        for i in index:
            if i!=0:
                return False
        return True