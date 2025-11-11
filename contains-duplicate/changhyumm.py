class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = True
        return False