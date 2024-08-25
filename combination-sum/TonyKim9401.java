class Solution {
    // time complexity: O(2^n);
    // space complecity: O(n*m);
    private List<List<Integer>> output = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        backtracking(candidates, 0, target, new ArrayList<>());
        return output;
    }

    public void backtracking(int[] candidates, int idx, int target, List<Integer> inside) {
        if (target == 0) {
            output.add(new ArrayList<>(inside));
            return;
        }

        if (idx > candidates.length - 1 || target < 0) return;

        inside.add(candidates[idx]);
        backtracking(candidates, idx, target - candidates[idx], inside);
        inside.remove(inside.size()-1);
        backtracking(candidates, idx+1, target, inside);
    }
}
