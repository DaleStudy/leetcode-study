class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        - 시간복잡도: O(n^2)
        - 공간복잡도: O(n)
        DFS 사용
        1. 모든 조합을 찾기
        2. 조합을 찾을 때, 중복된 조합을 방지하기
        """
        result = []

        def dfs(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return result
