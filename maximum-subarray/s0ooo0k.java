class Solution {
    public int maxSubArray(int[] nums) {
        int curr = nums[0];
        int maxSum = nums[0];

        for(int i=1; i<nums.length; i++) {
            curr = Math.max(nums[i], curr+nums[i]);
            maxSum = Math.max(maxSum, curr);
        }
        return maxSum;
    }
}

