import java.util.*;
class Solution {
    public List<List<Integer>> output;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        output = new ArrayList<>();
        Deque<Integer> stack = new ArrayDeque<>();
        dfs(candidates, target, stack, 0, 0);
        return output;

    }

    public void dfs(int[] candidates, int target, Deque<Integer> stack, int start, int total) {

        if (total > target) return;

        if (total == target) {
            output.add(new ArrayList<>(stack));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            int num = candidates[i];
            stack.push(num);
            dfs(candidates, target, stack, i, total + num);
            stack.pop();
        }
    }
}
