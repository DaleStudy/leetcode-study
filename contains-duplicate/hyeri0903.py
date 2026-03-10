class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = False
        dic = dict()

        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = 1
        return ans


