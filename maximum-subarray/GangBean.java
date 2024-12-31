class Solution {
    public int maxSubArray(int[] nums) {
        /**
        1. understanding
        - integer array nums
        - find largest subarray sum
        2. starategy
        - calculate cumulative sum
        - mem[i+1] = num[i+1] + mem[i] if (num[i+1] + mem[i] >= 0) else num[i+1]
        3. complexity
        - time: O(N)
        - space: O(1)
        */
        int prev = 0;
        int curr = 0;
        int max = Integer.MIN_VALUE;
        for (int i = 0 ; i < nums.length; i++) {
            curr = nums[i];
            if (prev >= 0) {
                curr += prev;
            }
            max = Math.max(max, curr);
            prev = curr;
        }
        return max;
    }
}

