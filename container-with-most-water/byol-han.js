/**
 * https://leetcode.com/problems/container-with-most-water/
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;
  let maxWater = 0;

  while (left < right) {
    let width = right - left; // 현재 너비는 두 포인터 사이 거리
    let minHeight = Math.min(height[left], height[right]); // 현재 높이는 두 선 중 더 낮은 값 (물이 넘치지 않기 위해 낮은 선 기준)
    let area = width * minHeight; // 현재 구간이 담을 수 있는 물의 양 계산

    maxWater = Math.max(maxWater, area); // 최대 물 저장량 갱신

    // 낮은 쪽 포인터를 이동시켜서 더 큰 높이를 찾음
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
};
