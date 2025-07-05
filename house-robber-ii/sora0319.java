class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];

        return Math.max(dp(nums, 0, nums.length - 1),
                        dp(nums, 1, nums.length));
    }

    private int dp(int[] nums, int start, int end) {
        int back = 0;
        int curr = 0;

        for (int i = start; i < end; i++) {
            int temp = curr;
            curr = Math.max(back + nums[i], curr);
            back = temp;
        }

        return curr;
    }
}
