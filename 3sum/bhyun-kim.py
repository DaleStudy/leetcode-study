"""
15. 3Sum
https://leetcode.com/problems/3sum/description/

Solution: 
    - Sort the list
    - Iterate through the list
    - For each element, find the two elements that sum up to -element
    - Use two pointers to find the two elements
    - Skip the element if it is the same as the previous element
    - Skip the two elements if they are the same as the previous two elements
    - Add the set to the output list

    Example:
        -----------------------------------------
        low :    |
        high:              |   
            i : |
                [-4,-1,-1,0,1,2]

        -----------------------------------------
        low :      |
        high:              |   
            i : |
                [-4,-1,-1,0,1,2]

                ... no possible set with i=-4, and high=2

        -----------------------------------------
        low :       |
        high:              |   
            i :     |
                [-4,-1,-1,0,1,2]


Time complexity: O(n^2)
    - O(nlogn) for sorting
    - O(n^2) for iterating through the list and finding the two elements
    - Total: O(n^2)
Space complexity: O(n)
    - O(n) for the output list
    - O(n) for the prevs dictionary
    - O(n) for the prevs_n set
    - Total: O(n)
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        prevs = dict()
        prevs_n = set()

        for i in range(len(nums) - 2):
            n_i = nums[i]

            if n_i in prevs_n:
                continue
            else:
                prevs_n.add(n_i)

            low, high = i + 1, len(nums) - 1
            while low < high:
                n_low = nums[low]
                n_high = nums[high]
                if n_i + n_low + n_high == 0:
                    if not f"[{n_i},{n_low},{n_high}]" in prevs:
                        prevs[f"[{n_i},{n_low},{n_high}]"] = 1
                        output.append([n_i, n_low, n_high])
                    low += 1
                    high -= 1

                elif n_i + n_low + n_high < 0:
                    low += 1

                elif n_i + n_low + n_high > 0:
                    high -= 1

        return output
