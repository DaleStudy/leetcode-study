from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, combination, candidateIndex):
            if remain == 0:
                # if we reach the target, add the combination to the result
                result.append(list(combination))
                return
            elif remain < 0:
                # if we exceed the target, no need to proceed
                return

            for i in range(candidateIndex, len(candidates)):
                # add the number to the current combination
                combination.append(candidates[i])
                # continue the exploration with the current number
                backtrack(remain - candidates[i], combination, i)
                # backtrack by removing the number from the combination
                combination.pop()

        result = []
        backtrack(target, [], 0)

        return result


# Time Complexity: O(N^(target / min(candidates)))
# The time complexity depends on:
# - N: The number of candidates (branching factor at each level).
# - target: The target sum we need to achieve.
# - min(candidates): The smallest element in candidates influences the maximum depth of the recursion tree.
# In the worst case, we branch N times at each level, and the depth can be target / min(candidates).
# Therefore, the overall time complexity is approximately O(N^(target / min(candidates))).

# Space Complexity: O(target / min(candidates))
# The space complexity is influenced by the maximum depth of the recursion tree:
# - target: The target sum we need to achieve.
# - min(candidates): The smallest element in candidates influences the maximum depth.
# The recursion stack can go as deep as target / min(candidates), so the space complexity is O(target / min(candidates)).
# Additionally, storing the results can take significant space, but it depends on the number of valid combinations found.
