var maxArea = function (height) {
  // Two pointer: left and right
  // Amount of water: math.Min(height[left], height[right]) * (right-left)

  // Eception case
  if (height.length === 0) return 0;

  let left = 0;
  let right = height.length - 1;
  let result = 0;

  // Iterate to find maxiume amount of water
  while (left < right) {
    const amount = Math.min(height[left], height[right]) * (right - left);
    result = Math.max(result, amount);
    height[left] <= height[right] ? left++ : right--;
  }

  return result;
};

// TC: O(n)
// SC: O(1)
