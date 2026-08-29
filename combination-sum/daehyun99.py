from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        que = deque([candidate] for candidate in candidates)
        while len(que) > 0:
            values = que.popleft()
            sum_values = sum(values)
            if sum_values == target:
                result.append(values)
                continue
            for candidate in candidates:
                if values[-1] > candidate:
                    continue
                if sum_values + candidate <= target:
                    temp = values.copy()
                    temp.append(candidate)
                    que.append(temp)
        return result
