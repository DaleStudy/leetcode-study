/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  // Two Pointer를 이용해서 문제를 접근해야할 것 같은데 두 포인터 중에 어떤 거를 이동시켜야하는지 이 부분이 고민이 됨.
  // 그래서 이 부분은 풀이 참고
  let maxArea = 0;
  let start = 0,
    end = height.length - 1;

  while (start < end) {
    // 가로 * 세로
    let area = (end - start) * Math.min(height[start], height[end]);

    maxArea = Math.max(area, maxArea);

    // 고민했던 지점
    if (height[start] < height[end]) {
      start++;
    } else {
      end--;
    }
  }
  return maxArea;
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
