"""
Problem: Two Sum

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

<Solution 1>
Time Complexity: O(n²)
- 중첩 반복문 사용
- 첫 번째 반복문: n번
- 각각에 대한 두 번째 반복문: n-1, n-2, ... 1번
- 총 연산 횟수: n * (n-1)/2
    
Space Complexity: O(1)
- 추가 공간을 사용하지 않음
- result는 항상 크기가 2로 고정됨
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

"""
<Solution 2: 해시 테이블 활용>
Time Complexity: O(n)
- 배열을 한 번만 순회

Space Complexity: O(n)
- 최악의 경우 해시 테이블에 n개를 저장
- 추가 공간이 입력 크기에 비례
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []

