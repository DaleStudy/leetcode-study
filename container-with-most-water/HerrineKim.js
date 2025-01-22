// 시간복잡도: O(n)
// 공간복잡도: O(1)

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let maxWater = 0;
  let left = 0;
  let right = height.length - 1;

  while (left < right) {
    const lowerHeight = Math.min(height[left], height[right]);
    const width = right - left;
    maxWater = Math.max(maxWater, lowerHeight * width);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
};
