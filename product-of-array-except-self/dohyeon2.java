import java.util.Arrays;

class Solution {
    // TC : O(n)
    // SC : O(n)
    public int[] productExceptSelf(int[] nums) {
        /**
         * Approach:
         * 1. Calculate the product of all non-zero elements
         * 2. Count how many zeros exist in the array.
         * 3. Handle three cases:
         * - If there are more than one zero, all results are 0.
         * - If there is exactly one zero,
         * only the index with 0 gets the total product; others are 0.
         * - If there is no zero, each result is totalProduct / nums[i].
         */
        int zeroCount = 0;

        for (int n : nums) {
            if (n == 0) {
                zeroCount++;
            }
            if (zeroCount > 1) {
                break;
            }
        }

        if (zeroCount > 1) {
            return new int[nums.length];
        }

        int production = Arrays.stream(nums).filter((n) -> {
            return n != 0;
        }).reduce(1, (a, b) -> a * b);

        if (zeroCount == 1) {
            return Arrays.stream(nums).map((n) -> {
                if (n == 0) {
                    return production;
                }
                return 0;
            }).toArray();
        }

        return Arrays.stream(nums).map((n) -> {
            return production / n;
        }).toArray();
    }
}
