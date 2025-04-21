class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(result,remain, path, start):
            if remain==0:
                result.append(path[:])
                return 
            if remain < 0:
                return 
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(result,remain - candidates[i], path, i)  
                path.pop()  

        dfs(result,target, [], 0)
        return result


