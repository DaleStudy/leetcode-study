from typing import List
from typing import Dict


class Solution:
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Make a map {target - num : index of num} with the list nums.
        # Time: O(n)
        # Space: O(n)
        mapOfSubtractedValueToIndex: Dict[int, int] = ({
            target - num: index for index, num in enumerate(nums)
        })
        
        # 2. ForEach num in nums, get value from the map.
        # Time: O(n)
        # Space: O(n)
        result: List[int] = None
        for indexOfNum, num in enumerate(nums):
            try:
                indexOfSubtractedValue = mapOfSubtractedValueToIndex[num]
                if indexOfSubtractedValue == indexOfNum:
                    continue
                # 3. Return the index of num in nums and the value from the map.
                return [indexOfNum, indexOfSubtractedValue]
            except KeyError: 
                continue
