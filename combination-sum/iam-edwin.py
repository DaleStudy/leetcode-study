from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = [[[] for _ in range(target + 1)] for _ in range(len(candidates))]

        for index in range(len(candidates)):
            num = candidates[index]
            for subTarget in range(1, target + 1):
                maxUseCount = subTarget // num
                for useCount in range(0, maxUseCount + 1):
                    subSubTarget = subTarget - num * useCount
                    if subSubTarget == 0:
                        result[index][subTarget].append([num] * useCount)
                    else:
                        for item in result[index - 1][subSubTarget]:
                            result[index][subTarget].append(item + [num] * useCount)

        return result[len(candidates) - 1][target]
