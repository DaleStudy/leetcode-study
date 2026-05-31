// tc: O(n);
// sc: O(1);
const maxArea = function (height) {
  let max = 0;
  let leftIdx = 0;
  let rightIdx = height.length - 1;

  while (leftIdx < rightIdx) {
    const width = rightIdx - leftIdx;
    const minHeight = Math.min(height[leftIdx], height[rightIdx]);
    const area = width * minHeight;
    max = Math.max(max, area);

    if (height[leftIdx] > height[rightIdx]) {
      rightIdx -= 1;
    } else {
      leftIdx += 1;
    }
  }

  return max;
};
