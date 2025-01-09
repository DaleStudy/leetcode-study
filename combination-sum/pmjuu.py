from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, current_combination):
            # 종료 조건
            if target == 0:
                result.append(list(current_combination))
                return
            if target < 0:
                return
            
            # 백트래킹
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, target - candidates[i], current_combination)  # 같은 원소를 여러 번 쓸 수 있도록 i를 그대로 둡니다.
                current_combination.pop()  # 돌아가서 다시 시도할 수 있도록 원소를 제거합니다.

        backtrack(0, target, [])

        return result


# 시간 복잡도: O(n^t)
# - 후보 리스트에서 각 숫자를 선택할 수 있기 때문에, n개의 후보를 사용해 t번의 탐색을 할 수 있습니다.
# - 따라서 최악의 경우 탐색 횟수는 O(n^t)로 볼 수 있습니다.
#
# 공간 복잡도: O(t)
# - 재귀 호출 스택의 깊이는 최대 target 값인 t에 비례하므로, 공간 복잡도는 O(t)입니다.
# - 또한, 현재까지 선택된 숫자들의 조합을 저장하는 공간도 최대 t개까지 저장하므로, 공간 복잡도는 O(t)입니다.
