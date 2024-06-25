/*
 * time: O(n^2)
 * space: O(n)
 */
class Solution {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> combination = new LinkedList<>();
        backtrack(candidates, target, combination, 0, result);
        return result;
    }

    void backtrack(int[] candidates, int remain, List<Integer> combination, int startIndex, List<List<Integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<>(combination));
            return;
        } else if (remain < 0) {
            return;
        }

        for (int i = startIndex; i < candidates.length; i++) {
            combination.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], combination, i, result);
            combination.removeLast();
        }
    }
}
