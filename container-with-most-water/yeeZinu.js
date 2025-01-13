/**
 * @param {number[]} height
 * @return {number}
 */

var maxArea = function (height) {
  let max = 0;                    // 최대값
  let left = 0;                   // 왼쪽 값
  let right = height.length - 1;  // 오른쪽 값

  // 왼쪽과 오른쪽을 하나씩 줄여가며 가운데서 만날 때 까지 반복
  while (left < right) {
    // 최대값 = 가로길이(오른쪽 값 - 왼쪽 값) * 세로길이(왼쪽 값, 오른쪽 값 중 더 작은 값)
    max = Math.max(max, (right - left) * Math.min(height[left], height[right]));
    // 오른쪽 세로가 더 높다면 왼쪽 값 증가
    if (height[left] < height[right]) {
      left++;
    }
    else {
      right--;
    }
  }
  return max;
};
