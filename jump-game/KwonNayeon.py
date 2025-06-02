"""
Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

<Solution 1>

Time Complexity: O(n)
- n은 배열의 길이만큼 한 번 순회

Space Complexity: O(1)
- 추가 공간 사용 없음

풀이방법: 
1. max_reach 변수로 현재까지 도달 가능한 최대 거리 저장
2. 배열을 순회하면서:
  - 현재 위치가 max_reach보다 크면 도달 불가능 
  - max_reach를 현재 위치에서 점프 가능한 거리와 비교해 업데이트
  - max_reach가 마지막 인덱스보다 크면 도달 가능
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = nums[0]

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

            if max_reach >= len(nums) - 1:
                return True

        return True

"""
<Solution 2>

Time Complexity: 
- 

Space Complexity: 
- 

풀이방법: 
"""

