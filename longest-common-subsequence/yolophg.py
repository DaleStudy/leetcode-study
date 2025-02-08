# Time Complexity: O(m * n) - each (i, j) pair is computed once and stored, reducing redundant calls.
# Space Complexity: O(m * n) - memoization dictionary stores O(m * n) states.
# - Recursion stack depth is O(m + n) in the worst case.

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        # to memoize results so we don't recompute the same subproblems
        m = dict()

        # recursive function to compute LCS
        def s(i, j):
            # base case: if we reach the end of either string, there's nothing left to compare
            if i == len(t1) or j == len(t2):
                return 0
            
            # if already computed this state, just return the cached value
            if (i, j) in m:
                return m[(i, j)]
            
            # if the characters match, we take this character and move diagonally
            if t1[i] == t2[j]:
                m[i, j] = 1 + s(i + 1, j + 1)
            else:
                # if they don't match, we either move forward in t1 or t2 and take the max
                m[i, j] = max(s(i + 1, j), s(i, j + 1))
            
            return m[i, j]

        return s(0, 0)
