import java.util.*;

class Solution {
    List<List<Integer>> answer = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        recur(new ArrayList<Integer>(), candidates, target, 0, 0);
        return answer;
    }

    public void recur(List<Integer> result, int[] candidates, int target, int sum, int index) {
        if (sum == target) {
            List<Integer> deepCopyRes = new ArrayList<>(result);
            answer.add(deepCopyRes);
            return;
        }
        for (int i = index; i < candidates.length; i++) {
            if (sum + candidates[i] <= target) {
                result.add(candidates[i]);
                recur(result, candidates, target, sum + candidates[i], i);
                result.remove(Integer.valueOf(candidates[i]));
            }
        }
    }
}
