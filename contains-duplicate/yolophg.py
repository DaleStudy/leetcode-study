# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set to keep track of duplicates.
        duplicates = set()

        # go through each number in the list
        for num in nums:
            # if it's a duplicate, return true.
            if num in duplicates:
                return True
            # otherwise, add it to the set to check for duplicates.
            duplicates.add(num)

        # if finish the loop and don't find duplicates, return false.
        return False
