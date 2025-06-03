"""
Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

<Solution 1>

Time Complexity: O(n)
- 배열을 한 번 순회 (배열의 길이 = n)

Space Complexity: O(1)
- 추가 공간 사용 없음

풀이방법:
- 그리디 알고리즘 활용
  - 매 지점에서 갈 수 있는 최대 거리만을 기록함
  - 각 위치에서 greedy하게 가장 멀리 갈 수 있는 거리를 계산함
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

Time Complexity: O(n^2)
- 최악의 경우 각 인덱스에서 모든 가능한 점프를 시도

Space Complexity: O(n)
- 메모이제이션 딕셔너리 + 재귀 호출 스택

풀이방법: 
- DFS + 메모이제이션 (백트래킹)
- 모든 가능한 점프 경로를 탐색하되 중복 계산을 방지함
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}  # 메모이제이션으로 최적화
        
        def dfs(index):
            # 끝에 도달했으면 True 반환
            if index >= len(nums) - 1:
                return True
                
            # 이미 계산했으면 결과를 재사용
            if index in memo:
                return memo[index]
            
            # 현재 위치에서 가능한 모든 점프를 시도함
            for jump in range(1, nums[index] + 1):
                if dfs(index + jump):
                    memo[index] = True
                    return True
            
            # 모든 점프를 시도해봐도 끝에 도달하지 못함
            memo[index] = False
            return False
        
        return dfs(0)

