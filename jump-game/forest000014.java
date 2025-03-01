/* 
# Time Complexity: O(n)
# Space Complexity: O(n)
*/

class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        boolean[] dp = new boolean[n];

        dp[0] = true;

        for (int i = 0; i < n; i++) {
            if (!dp[i]) return false;
            int j = Math.min(n - 1, i + nums[i]);
            for (; j >= i + 1; j--) {
                if (dp[j]) break;
                dp[j] = true;
            }
        }

        return true;
    }
}
