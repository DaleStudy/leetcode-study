# O(T) time, O(C^T) space
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results, nums = [], []

        def dfs(start, total):
            if total > target:
                return
            if total == target:
                results.append(nums[:])
            for i in range(start, len(candidates)):
                num = candidates[i]
                nums.append(num)
                dfs(i, total + num)
                nums.pop()
        
        dfs(0, 0)

        return results
