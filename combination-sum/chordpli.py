from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.__backtrack__(candidates, 0, target, result, [])
        return result

    def __backtrack__(self, candidates: List[int], current_idx: int, target: int, result: List[List[int]],
                      current_arr: List[int]):
        if current_idx >= len(candidates):
            return

        add_value = sum(current_arr) + candidates[current_idx]

        if add_value == target:
            current_arr.append(candidates[current_idx])
            result.append(current_arr.copy())
            current_arr.pop()

        if add_value > target:
            return self.__backtrack__(candidates, current_idx + 1, target, result, current_arr)

        current_arr.append(candidates[current_idx])
        self.__backtrack__(candidates, current_idx, target, result, current_arr)
        current_arr.pop()
        self.__backtrack__(candidates, current_idx + 1, target, result, current_arr)