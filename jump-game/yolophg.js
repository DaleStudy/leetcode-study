// Time Complexity: O(n)
// Space Complexity: O(1)

var canJump = function (nums) {
  // start from the last position
  let lastPos = nums.length - 1;

  // traverse the array from the end to the start
  for (let i = nums.length - 2; i >= 0; i--) {
    // if can jump from the current position to the lastPos or beyond
    if (i + nums[i] >= lastPos) {
      // move the lastPos to the current position
      lastPos = i;
    }
  }

  // if have moved lastPos to the start, can reach the end
  return lastPos === 0;
};
