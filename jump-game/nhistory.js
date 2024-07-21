var canJump = function (nums) {
  let pointer = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > pointer) return false;
    pointer = Math.max(pointer, i + nums[i]);
    if (pointer >= nums.length - 1) return true;
  }
  return false;
};

// TC: O(n)
// SC: O(1)
