/**
 * 11. Container With Most Water
 * You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
 * Find two lines that together with the x-axis form a container, such that the container contains the most water.
 * Return the maximum amount of water a container can store.
 *
 * Notice that you may not slant the container.
 *
 * https://leetcode.com/problems/container-with-most-water/description/
 *
 */

// O(n) time
// O(1) space
function maxArea(height: number[]): number {
  let l = 0;
  let r = height.length - 1;
  let max = 0;

  while (l < r) {
    max = Math.max(max, Math.min(height[l], height[r]) * (r - l));

    if (height[l] < height[r]) {
      l++;
    } else {
      r--;
    }
  }

  return max;
}
