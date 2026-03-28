import java.util.ArrayList;
import java.util.List;

class Solution {
    // TC : O(n!) => TC : O(2^T)
    // SC : O(n^2) => SC : O(T)
    ArrayList<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        backtrack(0, target, candidates, new ArrayList<>());
        return result;
    }

    private void backtrack(int start, int diff, int[] candidates, ArrayList<Integer> path) {
        if (diff == 0) {
            result.add(new ArrayList<>(path)); // 깊은 복사
            return;
        }

        if (diff < 0) {
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            path.add(candidates[i]);
            backtrack(i, diff - candidates[i], candidates, path);
            path.remove(path.size() - 1);
        }
    }
}
