// 처음엔 dp라 생각했는데, backtracking인걸 알아차리자마자 풀 수 있었음
// 중간 결과를 계속 전달하는게 팁
class Solution {
   public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtracking(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtracking(int[] candidates, int target, int start, List<Integer> tmp, List<List<Integer>> result) {
        if (target < 0) {
            return;
        }
        
        if (target == 0) {
            result.add(new ArrayList<>(tmp));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            tmp.add(candidates[i]); 
            backtracking(candidates, target - candidates[i], i, tmp, result);
            tmp.remove(tmp.size() - 1); 
        }
    }
}
