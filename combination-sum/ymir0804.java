import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
   public List<List<Integer>> combinationSum(int[] candidates, int target) {
       List<List<Integer>> result = new ArrayList<>();
       Arrays.sort(candidates);
       backtrack(candidates, target, new ArrayList<>(), result, 0);
       return result;
    }


    public void backtrack(int[] candidates, int remain, List<Integer> current, List<List<Integer>> result, int start) {
        if (remain < 0) {
            return;
        }
        if (remain == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < candidates.length; i++) {

            if (candidates[i] > remain) break;
            current.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], current, result, i);
            current.remove(current.size() - 1);
        }
    }
}
