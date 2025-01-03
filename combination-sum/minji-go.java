/*
    Problem: https://leetcode.com/problems/combination-sum/
    Description: return a list of all unique combinations of candidates where the chosen numbers sum to target
    Concept: Array, Backtracking
    Time Complexity: O(Nᵀ), Runtime 2ms 
    Space Complexity: O(T), Memory 44.88MB
*/
class Solution {
    public List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        findCombination(candidates, target, new ArrayList<>(), 0);
        return answer;
    }

    public void findCombination(int[] candidates, int target, List<Integer> combination, int idx) {
        if(target == 0) {
            answer.add(new ArrayList<>(combination));
            return;
        }

        for(int i=idx; i<candidates.length; i++) {
            if(candidates[i] > target) break;

            combination.add(candidates[i]);
            findCombination(candidates, target-candidates[i], combination, i);
            combination.remove(combination.size()-1);
        }
    }
}
