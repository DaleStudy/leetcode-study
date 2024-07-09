/*
    time: O(N)
    time: O(1)
 */
class Solution {

    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }

        return Math.max(
                dp(nums, 0, nums.length - 2),
                dp(nums, 1, nums.length - 1)
        );
    }

    private static int dp(int[] nums, int start, int end) {
        int maxOfOneStepAhead = nums[end];
        int maxOfTwoStepsAhead = 0;

        for (int i = end - 1; i >= start; --i) {
            int curr = Math.max(maxOfOneStepAhead, maxOfTwoStepsAhead + nums[i]);

            maxOfTwoStepsAhead = maxOfOneStepAhead;
            maxOfOneStepAhead = curr;
        }
        return maxOfOneStepAhead;
    }
}
