/*
시간복잡도: O(n)
공간복잡도: O(1)
포인터까지는 생각했으나, 그이후로는 해결법이 떠오르지 않아, 알고달레 풀이를 보고 해결.

*/
function maxArea(height: number[]): number {
  let maxArea = 0;
  let left = 0;
  let right = height.length - 1;

  while (left < right) {
    let area = (right - left) * Math.min(height[left], height[right]);

    if (maxArea < area) maxArea = area;

    if (height[left] > height[right]) {
      right -= 1;
    } else {
      left += 1;
    }
  }
  return maxArea;
}
