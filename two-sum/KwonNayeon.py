"""
Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.
    
Time Complexity: O(n²)
    - 중첩 반복문을 사용하기 때문
    - 첫 번째 반복문: n번
    - 각각에 대해 두 번째 반복문: n-1, n-2, ... 1번
    - 따라서 총 연산 횟수는 n * (n-1)/2로 O(n²)
    
Space Complexity: O(1)
    - 추가 공간을 사용하지 않음
    - result 리스트는 항상 크기가 2로 고정
"""
# Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

# Solution 2

