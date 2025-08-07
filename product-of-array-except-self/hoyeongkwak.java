/*
Time Complexity : O(n)
Space Complexity : O(n)
*/
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] results = new int[nums.length];
        Arrays.fill(results, 1);
        int before = 1;
        int after = 1;

        for (int i = 0; i < nums.length - 1; i++) {
            before = before * nums[i];
            results[i + 1] = results[i + 1] * before;
        }

        for (int i = nums.length - 1; i > 0; i--) {
            after = after * nums[i];
            results[i - 1] = results[i - 1] * after;
        }
        return results;
    }
}
