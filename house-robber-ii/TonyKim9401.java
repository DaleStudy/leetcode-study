// TC: O(n)
// visit all nums at least once
// SC: O(1)
// only constant memory space required
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];

        int prev = 0;
        int post = 0;
        int output1 = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            int temp = prev;
            prev = Math.max(post + nums[i], prev);
            post = temp;
        }
        output1 = prev;

        prev = 0;
        post = 0;
        int output2 = 0;
        for (int i = 1; i < nums.length; i++) {
            int temp = prev;
            prev = Math.max(post + nums[i], prev);
            post = temp;
        }
        output2 = prev;

        return Math.max(output1, output2);
    }
}
