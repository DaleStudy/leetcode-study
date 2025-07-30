class Solution:
    def containsDuplicate(self, nums) -> bool:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for v in dic.values():
            if v > 1:
                return True
        return False
