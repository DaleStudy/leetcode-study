/*
Time Complexity : O(c^t)
Space Complexity : O(t)
 */

class Solution {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> output = new ArrayList<>();
        Stack<Integer> nums = new Stack<>();
        dfs (candidates, output, target, nums, 0, 0);
        return output;
    }

    private void dfs(int[] candidates, List<List<Integer>> output, int target, Stack<Integer> nums, int start, int total) {
        // base case : pass
        if (target == total) {
            output.add(new ArrayList<>(nums));
            return;
        }
        // base case : fail
        if (target < total) {
            return;
        }
        
        for (int i = start ; i < candidates.length ; i++) {
            int num = candidates[i];
            nums.push(num);
            dfs(candidates, output, target, nums, i, total + num);
            nums.pop();
        }


    }
}
