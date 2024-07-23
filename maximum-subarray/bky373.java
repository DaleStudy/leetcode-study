// time: O(N)
// space: O(1)
class Solution {

    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int k = nums[i];
            currentSum = Math.max(k, currentSum + k);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
