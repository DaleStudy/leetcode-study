class Solution {
    public int[] productExceptSelf(int[] nums) {
        /**
            1. understanding
            - given integer array nums
            - product of which's all elements except that element
            - should be under O(N) time complexity
            - should not use division operation
            2. strategy
            - brute force: O(n^2)
                - for every elements, calculate product of other elements
                    - 1: 2 * [3 * 4]
                    - 2: 1 * [3 * 4]
                    - 3: [1 * 2] * 4
                    - 4: [1 * 2] * 3
            - dynamic programming
                - assign array mem to memorize product till that idx
                - mem memorize in ascending order product value and reverse order product value
            3. complexity
            - time: O(N)
            - space: O(N)
        */
        // 1. assign array variable mem
        int[][] mem = new int[nums.length][];
        for (int i = 0 ; i < nums.length; i++) {
            mem[i] = new int[2];
        }

        // 2. calculate product values
        for (int i = 0 ; i < nums.length; i++) { // O(N)
            if (i == 0) {
                mem[i][0] = nums[i];
                continue;
            }
            mem[i][0] = nums[i] * mem[i-1][0];
        }

        for (int i = nums.length - 1; i >= 0; i--) { // O(N)
            if (i == nums.length - 1) {
                mem[i][1] = nums[i];
                continue;
            }
            mem[i][1] = nums[i] * mem[i+1][1];
        }

        int[] ret = new int[nums.length];
        for (int i = 0; i < nums.length; i++) { // O(N)
            int left = (i - 1) >= 0 ? mem[i-1][0] : 1;
            int right = (i + 1) < nums.length ? mem[i+1][1] : 1;
            ret[i] = left * right;
        }

        return ret;
    }
}

