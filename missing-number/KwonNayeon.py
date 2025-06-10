""" 
Constraints:
 1. n equals the length of array nums
 2. n is between 1 and 10^4 inclusive 
 3. Each element nums[i] is between 0 and n inclusive
 4. All numbers in nums are unique (no duplicates)

 <Solution 1>
Time Complexity: O(nlogn)
- 정렬에 nlogn, 순회에 n이 필요하므로 전체적으로 O(nlogn)

Space Complexity: O(1)
- 추가 공간을 사용하지 않고 입력 배열만 사용

풀이 방법:
1. nums 배열을 오름차순으로 정렬
2. 0부터 n까지 순서대로 비교하여 인덱스와 다른 값을 찾음
  - 인덱스와 해당 위치의 값이 일치하지 않을 때, 그 인덱스가 missing number
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i == nums[i]:
                continue
            else:
                return i
        # missing number가 배열의 마지막에 오는 경우
        return n


