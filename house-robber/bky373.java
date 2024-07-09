/*
    time: O(N)
    space: O(1)
 */
class Solution {

    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int maxOfTwoStepsAhead = 0;
        int maxOfOneStepAhead = nums[nums.length - 1];

        for (int i = nums.length - 2; i >= 0; --i) {
            int curr = Math.max(maxOfOneStepAhead, maxOfTwoStepsAhead + nums[i]);

            maxOfTwoStepsAhead = maxOfOneStepAhead;
            maxOfOneStepAhead = curr;
        }
        return maxOfOneStepAhead;
    }
}
