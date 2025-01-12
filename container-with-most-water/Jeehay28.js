/**
 * @param {number[]} height
 * @return {number}
 */

// Time Complexity: O(n)
// Space Complexity: O(1)
var maxArea = function (height) {
  let start = 0;
  let end = height.length - 1;
  let maxArea = 0;

  while (start < end) {
    const area = (end - start) * Math.min(height[start], height[end]);
    maxArea = Math.max(area, maxArea);

    // The shorter height limits the area.
    // By moving the pointer associated with the shorter height,
    // the algorithm maximizes the chance of finding a taller line that can increase the area.
    // This is the essence of the two-pointer strategy for the container problem.
    if (height[start] < height[end]) {
      start += 1;
    } else {
      end -= 1;
    }
  }
  return maxArea;
};

