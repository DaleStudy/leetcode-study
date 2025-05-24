/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;
  let max = 0;

  while (left < right) {
    const graphW = right - left;
    const grapghH = Math.min(height[left], height[right]);

    max = Math.max(max, graphW * grapghH);

    if (height[left] <= height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return max;
};
