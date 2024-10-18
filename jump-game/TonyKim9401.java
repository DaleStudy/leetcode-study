// TC: O(n)
// SC: O(1)
class Solution {
    public boolean canJump(int[] nums) {
        int jump = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i > jump) return false;
            jump = Math.max(jump, i + nums[i]);
        }
        return true;
    }
}
