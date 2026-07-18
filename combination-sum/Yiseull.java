class Solution {

    private List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        dfs(candidates, target, 0, new ArrayList<>());
        return answer;
    }

    private void dfs(int[] candidates, int target, int start, List<Integer> combination) {
        if (target == 0) {
            answer.add(new ArrayList<>(combination));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > target) {
                break;
            }

            combination.add(candidates[i]);
            dfs(candidates, target - candidates[i], i, combination);
            combination.removeLast();
        }
    }
}
