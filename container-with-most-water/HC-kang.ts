/**
 * https://leetcode.com/problems/container-with-most-water/
 * T.C. O(n)
 * S.C. O(1)
 */
function maxArea(height: number[]): number {
  let [res, i, j] = [0, 0, height.length - 1];

  while (i < j) {
    const volume = Math.min(height[i], height[j]) * (j - i);
    res = Math.max(res, volume);

    if (height[i] < height[j]) {
      i++;
    } else {
      j--;
    }
  }

  return res;
}
