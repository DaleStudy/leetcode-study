import java.util.Arrays;

class Solution {
    // TC : O(n)
    // SC : O(n)
    public int[] productExceptSelf(int[] nums) {
        /**
         * I previously solved this problem using division,
         * but the problem restricts that approach.
         * This was pointed out in the following comment:
         * https://github.com/DaleStudy/leetcode-study/pull/2396#discussion_r2934545648
         *
         * Approach:
         * Compute prefix products using left[i-1] * nums[i-1],
         * which represents the product of elements before i.
         *
         * Compute suffix products using right[i+1] * nums[i+1]
         * by traversing from right to left.
         *
         * The result at index i is:
         * left[i] * right[i]
         */

        int[] answer = new int[nums.length];

        int[] left = new int[nums.length];
        Arrays.fill(left, 1);
        int[] right = new int[nums.length];
        Arrays.fill(right, 1);

        for (int i = 0; i < nums.length; i++) {
            if (i - 1 < 0)
                continue;
            left[i] *= left[i - 1] * nums[i - 1];
        }

        for (int i = nums.length - 1; i >= 0; i--) {
            if (i + 1 > nums.length - 1)
                continue;
            right[i] *= right[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < nums.length; i++) {
            answer[i] = left[i] * right[i];
        }

        return answer;
    }
}
