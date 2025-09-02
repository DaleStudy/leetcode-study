/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  // 더 낮은 쪽을 안쪽으로 이동하는 방식으로

  let start = 0;
  let end = height.length - 1;
  let res = -1;
  while (start <= end) {
    const v = Math.min(height[start], height[end]) * (end - start);
    if (v > res) {
      res = v;
    }

    if (height[start] > height[end]) {
      end -= 1;
    } else {
      start += 1;
    }
  }
  return res;
};
