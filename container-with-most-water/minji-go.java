/**
 * <a href="https://leetcode.com/problems/container-with-most-water/">week06-2.container-with-most-water</a>
 * <li>Description: Return the maximum amount of water a container can store</li>
 * <li>Topics: Array, Two Pointers, Greedy      </li>
 * <li>Time Complexity: O(N), Runtime 5ms       </li>
 * <li>Space Complexity: O(1), Memory 57.42MB   </li>
 */
class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            int width = right - left;
            int minHeight = Math.min(height[left], height[right]);
            maxArea = Math.max(maxArea, width * minHeight);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
