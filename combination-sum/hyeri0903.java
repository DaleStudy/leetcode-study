class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(candidates); //불필요한 탐색을 줄이기 위해 sorting
        dfs(0, candidates, target, new ArrayList<>(), answer);
        return answer;
        
    }

    public void dfs(int start, int[] candidates, int target, List<Integer> curList, List<List<Integer>> answer) {
        if (target == 0) {
            answer.add(new ArrayList<>(curList));
            return;
        }
        for(int i = start; i < candidates.length; i++) {
            if (candidates[i] > target) {
                break;
            }
            
            curList.add(candidates[i]);
            dfs(i, candidates, target - candidates[i], curList, answer);
            curList.remove(curList.size()-1); //다음 경우의 수를 위해 backtracking

        }
    }
}
