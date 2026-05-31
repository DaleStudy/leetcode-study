# idea: brute force
# Complexity: O(len(candidates)^(target / min(candidates)))

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        nums = []

        def dfs(start: int, total: int):
            if total > target:
                return
            if total == target:
                result.append(nums.copy())
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if total + num > target:
                    break
                nums.append(num)
                dfs(i, total + num) 
                nums.pop()
        dfs(0, 0)
        return result
    


