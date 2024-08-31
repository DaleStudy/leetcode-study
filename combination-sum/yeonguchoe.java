class Solution {
    // Time complexity: O(candidate^(target/smallest candidate))
    // Space complexity: O(target/smallest candidate)

    List<List<Integer>> result = new ArrayList<>();

    public void backtracking(int remainingAmount, List<Integer> combination, int startPoint, int[] candidateList,
            List<List<Integer>> resultList) {
        if (remainingAmount == 0) {
            resultList.add(new ArrayList<>(combination));
            return;
        }

        if (remainingAmount < 0) {
            return;
        }

        for (int i = startPoint; i < candidateList.length; i++) {
            combination.add(candidateList[i]);
            backtracking(remainingAmount - candidateList[i], combination, i, candidateList, resultList);
            combination.remove(combination.size() - 1);
        }
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        ArrayList<Integer> initialCombination = new ArrayList<>();
        backtracking(target, initialCombination, 0, candidates, result);
        return result;
    }
}
