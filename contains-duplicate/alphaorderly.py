class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = set()
        for num in nums:
            if num in counter:
                return True
            else:
                counter.add(num)
        return False
