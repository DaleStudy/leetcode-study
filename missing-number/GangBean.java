class Solution {
    public int missingNumber(int[] nums) {
        /**
        1. understanding
        - array nums, n distinct numbers in range [0, n]
        - find missing number
        2. strategy
        - you can calculate the sum of range [0, n]: n(n+1)/2 ... (1)
        - and the sum of nums ... (2)
        - and then extract (2) from (1) = (missing value) what we want.
        3. complexity
        - time: O(N), N is the length of nums
        - space: O(1)
        */
        int N = nums.length;
        return N*(N+1)/2 - Arrays.stream(nums).sum();
    }
}

