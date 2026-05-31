class Solution {
    public int rob(int[] nums) {
        int money = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                money += nums[i];
            }
        }
        return money;
    }
}
