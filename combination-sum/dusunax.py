'''
# 39. Combination Sum

Backtracking for find combinations.

## Time and Space Complexity

```
TC: O(n^2)
SC: O(n)
```

#### TC is O(n^2):
- iterating through the list in backtracking recursion to find combinations. = O(n^2)

#### SC is O(n):
- using a list to store the combinations. = O(n)
'''

class Solution:
    # Backtracking = find combination
    # candidate is distinct & can use multiple times.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  

        def backtrack(currIdx, remain, combination):
            if(remain == 0):
                result.append(combination[:])
                return
            if(remain < 0):
                return

            for i in range(currIdx, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, remain - candidates[i], combination) 
                combination.pop()

        backtrack(0, target, [permutations])
        return result
