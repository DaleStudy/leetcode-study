/**
 * @description
 * brainstorming:
 * 1. brute force -> time limited
 * 2. two pointer
 *
 * n: length of height
 * time complexity: O(n)
 * space complexity: O(1)
 */
var maxArea = function (height) {
  let answer = 0;
  let start = 0;
  let end = height.length - 1;

  while (start !== end) {
    const w = end - start;
    const h = Math.min(height[start], height[end]);
    answer = Math.max(answer, w * h);
    if (height[start] >= height[end]) {
      end--;
    } else if (height[start] < height[end]) {
      start++;
    }
  }

  return answer;
};
