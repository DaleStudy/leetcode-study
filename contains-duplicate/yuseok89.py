class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_check = set()

        for num in nums:
            if num in dup_check:
                return True

            dup_check.add(num)

        return False
