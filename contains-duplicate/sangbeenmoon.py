# time : O(n)
# space : O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = True
        return False
