class Solution:
    def combinationSum(self, candidates, target):
        output, nums = [], []
        def dfs(start, total):
            if total > target:
                return
            if total == target:
                return output.append(nums[:])
            for i in range(start, len(candidates)):
                num = candidates[i]
                nums.append(num)
                dfs(i, total + num)
                nums.pop()
        dfs(0, 0)
        return output
