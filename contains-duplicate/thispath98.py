"""
# Time Complexity: O(N)
- N번 순회
# Space Compelexity: O(N)
- 최악의 경우 (중복된 값이 없을 경우) N개 저장
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = True
            else:
                return True
        return False
