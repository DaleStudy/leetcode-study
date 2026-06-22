// Brute Force
// Time Complexity: O(n^2)
// Space Complexity: O(1)
const maxAreaBrute = (height) => {
  let maxWater = 0;
  for (let i = 0; i < height.length; i++) {
    for (let j = i + 1; j < height.length; j++) {
      const area = Math.min(height[i], height[j]) * (j - i);
      maxWater = Math.max(maxWater, area);
    }
  }
  return maxWater;
};

// Two Pointer
// Time Complexity: O(n)
// Space Complexity: O(1)
const maxArea = (height) => {
  let left = 0;
  let right = height.length - 1;
  let maxWater = 0;

  while (left < right) {
    const area = Math.min(height[left], height[right]) * (right - left);

    maxWater = Math.max(maxWater, area);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
};
