/**
 * <a href="https://leetcode.com/problems/jump-game/">week10-4. jump-game</a>
 * <li>Description: Return true if you can reach the last index, or false otherwise</li>
 * <li>Topics: Array, Dynamic Programming, Greedy           </li>
 * <li>Time Complexity: O(N), Runtime 2ms                   </li>
 * <li>Space Complexity: O(1), Memory 45.66MB               </li>
 */
class Solution {
    public boolean canJump(int[] nums) {
        int jump = 0;
        for (int i = 0; i <= jump; i++) {
            jump = Math.max(jump, i + nums[i]);
            if (jump >= nums.length - 1) {
                return true;
            }
        }
        return false;
    }
}
