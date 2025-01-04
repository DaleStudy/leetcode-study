"""
Solution: 
    1) 배열 정렬
    2) 0부터 for 문을 돌리는데 index 와 값이 다르면 return index
    3) 끝까지 일치한다면 return 배열의 크기 
Time: O(nlogn) = O(nlogn) + O(n)
Space: O(1)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
