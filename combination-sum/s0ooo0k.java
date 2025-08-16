class Solution {
    List<List<Integer>> result = new ArrayList<>();
    int[] candidates;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.candidates=candidates;
        backtrack(new ArrayList<>(), target, 0);
        return result;
    }
    void backtrack(List<Integer> comb, int remain, int start) {
        if(remain==0) {
            result.add(new ArrayList<>(comb));
            return;
        }
        if(remain<0) return;
        for(int i=start; i<candidates.length; i++) {
            comb.add(candidates[i]);
            backtrack(comb, remain-candidates[i], i);
            comb.remove(comb.size() - 1);
        }
    }
}

