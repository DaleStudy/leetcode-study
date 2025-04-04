class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for i in nums:
            if temp.get(i):
                return True
            else:
                temp[i] = True
        return False
