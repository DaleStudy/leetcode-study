import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> output = new ArrayList<>();
        Stack<Integer> nums = new Stack<>();
        dfs(candidates, output, nums, target, 0, 0);

        return output;
    }

    private void dfs(int[] candidates, List<List<Integer>> output, Stack<Integer> nums, int target, int start, int total) {
        if (total > target) {
            return;
        }
        if (total == target) {
            output.add(new ArrayList<>(nums));
        }
        for (int i=start; i<candidates.length; i++) {
            int num = candidates[i];
            nums.push(num);
            dfs(candidates, output, nums, target, i, total + num);
            nums.pop();
        }
    }
}
