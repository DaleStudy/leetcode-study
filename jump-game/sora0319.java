public class Solution {
    public boolean canJump(int[] nums) {
        int longLength = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > longLength) return false;
            longLength = Math.max(longLength, i + nums[i]);
        }
        return true;
    }
}