class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visit = set()

        for num in nums:
            if num in visit:
                return True

            visit.add(num)

        return False
