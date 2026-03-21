class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // dfs & 백트래킹
        List<List<Integer>> resultList = new ArrayList<>();
        dfs(candidates, target, 0, new ArrayList<>(), resultList);
        return resultList;
    }
    private void dfs(int[] candidates, int target, int start, List<Integer> path, List<List<Integer>> resultList) {
        if (target == 0) {
            resultList.add(new ArrayList<>(path));
            return;
        }

        if (target < 0) {
            return;
        }

        for(int i = start; i < candidates.length; i++) {
            path.add(candidates[i]);
            dfs(candidates, target - candidates[i], i, path, resultList);
            path.remove(path.size() -1);
        }
    }
}
