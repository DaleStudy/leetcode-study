import java.util.*; 
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>(); 
        List<Integer> temp = new ArrayList<>(); 

        backtrack(candidates, target, 0, temp, result);
        return result; 
    }
    private void backtrack(int[] candidates, int target, int start, List<Integer> temp, List<List<Integer>> result) {
        if (target < 0) return; 
        if (target == 0) {
            result.add(new ArrayList<>(temp)); // deep copy
            return; 
        }

        for (int i = start; i < candidates.length; i++) {
            temp.add(candidates[i]); 
            backtrack(candidates, target - candidates[i], i, temp, result); 
            temp.remove(temp.size() -1); 
        }

    }
}

/**
Return all unique combinations where the candidate num sum to target
- each num in cand[] can be used unlimited times 
- order of num in comb does NOT matter 

1. use backtracking to explore all possible comb 
2. backtrack, if current sum > target
3. save comb, if current sum == target 
4. avoid dupl -> only consider num from crnt idx onward (no going back)

Time: O(2^target)
Space: O(target)

Learned: Backtracking vs DFS
- DFS: search all paths deeply (no conditions, no rollback).
- Backtracking = DFS + decision making + undo step.
Explore, prune (if invalid), save (if valid), then undo last choice.

    for (선택 가능한 숫자 하나씩) {
        선택하고
        target 줄이고 (목표 가까워짐)
        재귀 호출로 다음 선택
        실패하거나 성공하면 되돌리기 (백트래킹)
    }

DFS just visits everything,
Backtracking visits only what’s promising — and turns back if not!
 */