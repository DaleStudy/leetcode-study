"""
https://leetcode.com/problems/contains-duplicate/
"""
# - time complexity : O(n)
# - space complexity : O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for n in nums:
            if n in visited:
                return True
            visited[n] = True
        return False
