class Solution {
    // * can't rob two adj houses in the same night
    // * return: max amount of money robbale in one night
    public int rob(int[] nums) {
        if(nums.length == 1) return nums[0];
        if(nums.length == 2) return Math.max(nums[0], nums[1]);

        // maxSum[i] = max sum possible at i (inclusive)
        int[] maxSum = new int[nums.length];
        maxSum[0] = nums[0];
        maxSum[1] = nums[1];

        for(int i = 2; i < nums.length; i++) {
            if(i == 2) {
                maxSum[i] = nums[i] + maxSum[i-2];
                continue;
            }

            // adj houses(i-1) can't be robbed
            // choices are:
            // 1. i-2 th house (choosing without skipping a house)
            // 2. i-3 th house (choosing with skipping a house)
            //    * choosing < i-4 th houses wouldn't be optimal because it'll be missing either of 1. or 2.
            maxSum[i] = nums[i] + Math.max(maxSum[i-2], maxSum[i-3]);
        }

        return Math.max(maxSum[nums.length-2], maxSum[nums.length-1]);
    }
}