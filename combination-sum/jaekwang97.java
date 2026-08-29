import java.util.*;
class Solution {
    private final List<List<Integer>> answers = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        answers.clear();
        Arrays.sort(candidates);
        dfs(new ArrayList<>(), 0, 0, target, candidates);
        return answers;
    }
    private void dfs(List<Integer> list, int sum, int start, int target, int[] candidates) {
        if (sum == target) {
            answers.add(new ArrayList<>(list));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (sum + candidates[i] > target) break;
            list.add(candidates[i]);
            dfs(list, sum + candidates[i], i, target, candidates);
            list.remove(list.size() - 1);
        }
    }
}
