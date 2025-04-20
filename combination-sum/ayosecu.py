from typing import List

class Solution:
    """
        - Time Complexity: O(2^t), t = target
            - This combination makes binary tree (t = Height)
            - The number of node in binary tree is 2^t
        - Space Complexity: O(t) => O(1)
            - backtrack function calls stack size (Tree's Height = t)
            - 1 <= t <= 40 => O(t) => O(40) => O(1)
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, target, start):
            if target == 0:
                result.append(list(path))
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(path, target - candidates[i], i)
                path.pop()

        backtrack([], target, 0)

        return result

tc = [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, [])
]

for i, (c, t, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.combinationSum(c, t)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
