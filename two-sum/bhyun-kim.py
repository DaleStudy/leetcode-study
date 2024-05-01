"""
Solution

Algorithm:
    1. Create a hashmap to store the index of each element.
    2. Iterate through the list.
    3. Check if the remaining value is in the hashmap.
    4. If it is, return the current index and the index of the remaining value in the hashmap.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in hashmap:
                return [i, hashmap[remaining]]

            hashmap[nums[i]] = i

def main():
    test_cases = [
        [2,7,11,15], 9, [0,1],
        [3,2,4], 6, [1,2],
        [3,3], 6, [0,1]
    ]
    s = Solution()
    
    for test_case in test_cases:
        nums_input, target_input, expected = test_case
        assert sorted(s.twoSum(nums_input, target_input)) == expected

if __name__ == '__main__':
    main()