/**
 * <a href="https://leetcode.com/problems/combination-sum/">week03-3.combination-sum</a>
 * <li>Description: return a list of all unique combinations of candidates where the chosen numbers sum to target </li>
 * <li>Topics: Array, Backtracking              </li>
 * <li>Time Complexity: O(K^T), Runtime 2ms     </li>
 * <li>Space Complexity: O(T), Memory 44.9MB    </li>
 */

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> combinations = new ArrayList<>();
        Arrays.sort(candidates);
        dfs(candidates, target, 0, new ArrayList<>(), combinations);
        return combinations;
    }

    public void dfs(int[] candidates, int target, int index, List<Integer> combination, List<List<Integer>> combinations) {
        if (target == 0) {
            combinations.add(new ArrayList<>(combination));
            return;
        }

        for (int i = index; i < candidates.length; i++) {
            if (target - candidates[i] < 0) break;

            combination.add(candidates[i]);
            dfs(candidates, target - candidates[i], i, combination, combinations);
            combination.remove(combination.size() - 1);
        }
    }
}
