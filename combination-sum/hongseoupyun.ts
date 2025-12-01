// Input: candidates = [2,3,5], target = 8
// Output: [[2,2,2,2],[2,3,3],[3,5]]

// DFS/backtracking should be used - Find possilbe combinations till the end and backtrack to previous step to find other combinations
// For example, if we have candidates [2,3,5] and target 8
// Start with empty combination [], target 8
// Add 2 -> [2], remaining 6
// Add 2 -> [2,2], remaining 4
// Add 2 -> [2,2,2], remaining 2
// Add 2 -> [2,2,2,2], remaining 0 (found a valid combination)
// Backtrack to [2,2,2,3], remaining -1 (remaining is negative, backtrack)
// Backtrack to [2,2,2,5], remaining -3 (remaining is negative, backtrack)
// Backtrack to [2,2,3], remaining 1 (dead end, backtrack)
// Backtrack to [2,2,5], remaining -3 (remaining is negative, backtrack)
// Backtrack to [2,3], remaining 3
// Add 3 -> [2,3,3], remaining 0 (found a valid combination)
// so on ..

// When you dfs, always start from current index and allow reusing the same element or next index only to avoid duplicates / to get unique combination
// Hence, if we starts from 2, next dfs calls can start from index of 2 or index of 3, but not index of 5 directly
// Moreover, if we start from 3, next dfs calls can start from index of 3 or index of 5, but not index of 2 directly

/*
backtrack(8, [], 0)
│
├─ i = 0 pick 2 → backtrack(6, [2], 0)
│   │
│   ├─ i = 0 pick 2 → backtrack(4, [2,2], 0)
│   │   │
│   │   ├─ i = 0 pick 2 → backtrack(2, [2,2,2], 0)
│   │   │   │
│   │   │   ├─ i = 0 pick 2 → backtrack(0, [2,2,2,2], 0) 🟢 success → return
│   │   │   │
│   │   │   ├─ i = 1 pick 3 → backtrack(-1, [2,2,2,3], 1) 🔴 → return
│   │   │   │
│   │   │   └─ i = 2 pick 5 → backtrack(-3, [2,2,2,5], 2) 🔴 → return
│   │   │
│   │   └─ loop end → pop → combination = [2,2]
│   │
│   ├─ i = 1 pick 3 → backtrack(1, [2,2,3], 1)
│   │   │
│   │   ├─ i = 1 pick 3 → backtrack(0, [2,2,3,3], 1) 🟢 success → return
│   │   │
│   │   └─ i = 2 pick 5 → backtrack(-4, [2,2,3,5], 2) 🔴 → return
│   │
│   ├─ loop end → pop → [2,2]
│   │
│   └─ i = 2 pick 5 → backtrack(-1, [2,2,5], 2) 🔴 → return
│
├─ loop end → pop → [2]
│
├─ i = 1 pick 3 → backtrack(3, [2,3], 1)
│   │
│   ├─ i = 1 pick 3 → backtrack(0, [2,3,3], 1) 🟢 success → return
│   │
│   └─ i = 2 pick 5 → backtrack(-2, [2,3,5], 2) 🔴 → return
│
├─ loop end → pop → [2]
│
├─ i = 2 pick 5 → backtrack(1, [2,5], 2)
│       │
│       └─ i = 2 pick 5 → backtrack(-4, [2,5,5], 2) 🔴 → return
│
└─ loop end → pop → []
*/


function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = []

    function backtrack(remaining: number, combination: number[], startindex: number) {
        // Remaining is target - sum of combination
        // Base Case1: If remaining is 0, we found a valid combination -> add that combinations to result
        if (remaining === 0) {
            result.push([...combination]);
            return;
        }

        // Base Case2: If remaining is negative, no valid combination -> backtrack
        if (remaining < 0) {
            return;
        }

        // Explore further by trying each candidate starting from startindex
        // candidates = [2,3,5], target = 8
        for (let i = startindex; i < candidates.length; i++) {
            // Choose the current number
            const currentNumber = candidates[i];
            // Add the current number to the combination
            combination.push(currentNumber);

            // Explore further with updated remaining and current combination
            backtrack(remaining - currentNumber, combination, i);
            // Backtrack: remove the last added candidate to try next candidate
            combination.pop();
        }
    }
        backtrack(target, [], 0);
        return result;
};
