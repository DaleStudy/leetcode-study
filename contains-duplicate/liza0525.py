class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_set = set()
        for num in nums:
            if num in check_set:
                return True
            check_set.add(num)
        return False
