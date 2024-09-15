/**
 * TC: O(H)
 * SC: O(1)
 * H: height.length
 */

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let maximumWater = 0;
  let left = 0;
  let right = height.length - 1;

  // 1. 투포인터를 이용하여 양끝에서 모입니다.
  while (left < right) {
    // 2. 최대 너비값을 갱신해주고
    const h = Math.min(height[left], height[right]);
    const w = right - left;

    maximumWater = Math.max(maximumWater, w * h);

    // 3. 왼쪽과 오른쪽 높이 중 더 낮은 쪽의 pointer를 옮깁니다.
    if (height[left] < height[right]) {
      left += 1;
    } else {
      right -= 1;
    }
  }

  return maximumWater;
};
