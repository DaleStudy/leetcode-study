import java.util.*;
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> output = new ArrayList<>();
        List<Integer> sum = new ArrayList<>();
        checkTarget(candidates, target, 0, output, sum);
        return output;
    }

    private void checkTarget(int[] candidates, int target, int start, List<List<Integer>> output, List<Integer> sum) {
        if (target == 0) {
            output.add(new ArrayList<>(sum));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            int current = candidates[i];
            if (current > target) continue;

            sum.add(current);
            checkTarget(candidates, target - current, i, output, sum);
            sum.remove(sum.size() - 1);
        }
    }
}


