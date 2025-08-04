class Solution {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int total = 0;

        for (int n : nums) {
            if (total < 0) {
                total = 0;
            }
            total += n;
            res = Math.max(total, res);

        }
        return res;
    }
}
