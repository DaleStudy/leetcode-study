import java.util.*;

// TC: O(n^(target/min))
// SC: O(target/min)
class Solution {
    private static List<List<Integer>> answer;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        answer = new ArrayList<>();

        List<Integer> bucket = new ArrayList<>();
        int curSum = 0;

        dfs(candidates, bucket, target, 0, 0);

        return answer;
    }

    private void dfs(int[] candidates, List<Integer> bucket, int target, int startIdx, int curSum) {
        if (curSum == target) {
            answer.add(new ArrayList<>(bucket));
            return;
        }
        if (curSum > target)
            return;

        for (int i = startIdx; i < candidates.length; i++) {
            bucket.add(candidates[i]);
            dfs(candidates, bucket, target, i, curSum + candidates[i]);
            bucket.removeLast();
        }

    }
}
