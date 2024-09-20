function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let maxSize = 0;

  while (left < right) {
    maxSize = Math.max(maxSize, getMaxSize(height, left, right));

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxSize;
}

function getMaxSize(height: number[], left: number, right: number) {
  return Math.min(...[height[right], height[left]]) * (right - left);
}

// TC: O(n)
// SC: O(1)
