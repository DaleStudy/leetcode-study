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
 1. 배열을 정렬하여 0부터 n까지 순서대로 있어야 할 위치에 없는 숫자를 찾음
 2. 인덱스와 해당 위치의 값을 비교하여 다르다면 그 인덱스가 missing number
 3. 모든 인덱스를 확인했는데도 없다면 n이 missing number
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i
         
        return len(nums)

'''
<Solution 2>

Time Complexity: 
- 

Space Complexity:
- 

풀이 방법:
'''
