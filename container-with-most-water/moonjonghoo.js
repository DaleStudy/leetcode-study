/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let max_area = 0;
  let left = 0;
  let right = height.length - 1;
  while (left < right) {
    let current_x = right - left;
    let current_y = Math.min(height[left], height[right]);
    let current_area = current_x * current_y;

    if (current_area > max_area) {
      max_area = current_area;
    }
    if (height[left] < height[right]) {
      left = left + 1;
    } else {
      right = right - 1;
    }
  }
  return max_area;
};

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
