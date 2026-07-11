# https://leetcode.com/problems/combination-sum/

# [접근]
# 처음에는 1부터 target 까지 결과를 저장하는 dp를 떠올렸다. 이 문제는 조합의 개수를 구하는게 아니라 전체 후보군을 구하는 문제이기 때문에 dfs로 백트래킹하도록 접근법을 바꿨다.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        size = len(candidates)

        # start_idx: 탐색 시작 인덱스
        # total: 현재까지의 합
        # combination: 선택된 숫자들 배열
        def dfs(start_idx: int, total: int, combination: List[int]) -> None:
            # 합이 target과 같으면 정답 배열에 추가하고 종료
            if total == target:
                result.append(combination)
                return

            # 합이 target 넘었으면 종료 
            if total > target:
                return 

            # 숫자를 여러번 사용할 수 있으므로 반복문을 start_idx 부터 시작한다.
            for i in range(start_idx, size):
                num = candidates[i]
                dfs(
                    i, 
                    total + num, # num 을 더한 합으로 호출
                    combination + [num]) # deep copy된 combination을 인자로 넘긴다.

        dfs(0, 0, [])

        return result


# 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        size = len(candidates)

        def dfs(start_idx: int, total: int, combination: List[int]) -> None:
            if total == target:
                # 결과에 추가할 때 combination 복사 
                result.append(combination.copy())
                return

            if total > target:
                return 

            for i in range(start_idx, size):
                num = candidates[i]
                
                # 반환 전 num 추가
                # -> 정답 찾으면 result에 추가할 때 combination deep copy 필요
                combination.append(num)

                dfs(i, total + num, combination)

                # 반환 후에 num 제거
                combination.pop()


        dfs(0, 0, [])

        return result

# 위 풀이와 거의 유사하다.
# 백트래킹시에 배열이 매번 깊은 복사되는 비효율이 있어서 result 배열에 담을 때만 복사하도록 했다.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        size = len(candidates)

        # start_idx: 탐색 시작 인덱스
        # total: 현재까지의 합
        # combination: 선택된 숫자들 배열
        def dfs(start_idx: int, total: int, combination: List[int]) -> None:
            # result 
            if total == target:
                result.append(combination.copy())
                return

            # 합이 target 넘었으면 종료 
            if total > target:
                return 

            # 숫자를 여러번 사용할 수 있으므로 반복문을 start_idx 부터 시작한다.
            for i in range(start_idx, size):
                num = candidates[i]

                # 반환 전 num 추가
                # -> 정답 찾으면 result에 추가할 때 combination deep copy 필요
                combination.append(num)

                dfs(i, total + num, combination)

                # 반환 후에 num 제거
                combination.pop()

        dfs(0, 0, [])

        return result
