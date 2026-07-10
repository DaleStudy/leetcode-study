import java.util.*;

class Solution {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];

        int currentStart = 0;
        int maxStart = 0;
        int maxEnd = 0;

        for (int i=1; i<nums.length; i++) {
            if (nums[i] > currentSum + nums[i]) {
                currentSum = nums[i];
                currentStart = i;
            } else {
                currentSum += nums[i];
            }

            if (currentSum > maxSum) {
                maxSum = currentSum;
                maxStart = currentStart;
                maxEnd = i;
            }
        }

        return maxSum;

    }
}
