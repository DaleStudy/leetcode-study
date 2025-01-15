// n: len(height)
// Time complexity: O(n)
// Space complexity: O(1)

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  const n = height.length;
  let left = 0;
  let right = n - 1;
  let answer = 0;

  while (left < right) {
    const w = right - left;
    const h = Math.min(height[left], height[right]);

    answer = Math.max(w * h, answer);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return answer;
};
