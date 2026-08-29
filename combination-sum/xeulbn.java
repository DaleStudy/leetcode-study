import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();

        backtrack(candidates, target, 0, new ArrayList<>(), result);

        return result;
    }

    private void backtrack(int[] candidates, int remain, int start, List<Integer> current, List<List<Integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        if (remain < 0) {
            return;
        }

        for (int i=start; i<candidates.length; i++) {
            int candidate = candidates[i];

            current.add(candidate);
            backtrack(candidates, remain - candidate, i, current, result);
            current.remove(current.size() - 1);
        }
    }
}
