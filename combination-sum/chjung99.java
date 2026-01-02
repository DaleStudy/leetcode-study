class Solution {
    Set<List<Integer>> combination = new HashSet<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        findCombination(candidates, target, 0, 0, new ArrayList<>());
        return new ArrayList<>(combination);
    }

    public void findCombination(int[] candidates, int target, int curIdx, int curSum, List<Integer> curList) {
        if (curSum == target) {
            combination.add(new ArrayList<>(curList));
            return;
        }

        if (curSum > target) {
            return;
        }

        for (int i = curIdx; i < candidates.length; i++){

            curList.add(candidates[i]);
            findCombination(candidates, target, i, curSum + candidates[i], curList);
            curList.remove(curList.size()-1);
        }
    }
}



