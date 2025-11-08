class Solution:
    def rob(self, nums: list[int]) -> int:
        hash_value = {}
        
        def dfs(start):
            if start in hash_value:
                return hash_value[start]
            
            if not start < len(nums):
                hash_value[start] = 0
            else:
                hash_value[start] = max(nums[start] + dfs(start+2), dfs(start+1))
            return hash_value[start]

        return dfs(0)

""" 
================================================================================
풀이 과정
================================================================================

1. 양 옆을 제외한 숫자들의 합을 구해야하네?
2. 첫 번째를 선택하면 → 세 번째 ~ N번째 들의 부분합을 구하는 것
3. 두 번째를 선택하면 → 네 번째 ~ N번째 들의 부분합을 구하는 것
4. 뭔가 재귀적으로 구할 수 있을 것 같은데..?
5. 첫 번째 선택한 것과 두 번째 선택한 것 중 어느것이 더 큰지 비교해보면 될 것 같은데?
6. 첫 번째를 선택한 것은 → nums[0] + 재귀(nums[2:])
7. 두 번째를 선택한 것은 → 재귀(nums[1:])
8. 그럼 재귀함수의 로직은 어떻게 되어야하지?


[1차 시도] 순수 재귀 - 시간 초과
────────────────────────────────────────────────────────────────────────────────
9. 기본적인 재귀 구조 구현

        def dfs(start):
            if start >= len(nums):
                return 0
            return max(nums[start] + dfs(start + 2), dfs(start + 1))

        return dfs(0)

10. 시간 초과가 발생했네?


11. 중간 결과값들을 저장하고 있어야할 것 같은데
12. 해싱으로 저장해놓고 있어보자

        hash_value = {}
        
        def dfs(start):
            if start in hash_value:
                return hash_value[start]
            
            if not start < len(nums):
                hash_value[start] = 0
            else:
                hash_value[start] = max(nums[start] + dfs(start+2), dfs(start+1))
            return hash_value[start]

        return dfs(0)

13. 정상적으로 통과되는 것 확인 완료
"""
