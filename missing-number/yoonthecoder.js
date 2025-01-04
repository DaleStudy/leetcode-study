var missingNumber = function (nums) {
  // store all the elemenst from nums in a Set
  const set = new Set(nums);

  // check the missing number by iterating through the index
  for (i = 0; i <= nums.length; i++) {
    if (!set.has(i)) {
      return i;
    }
  }
};

// Time complexity: O(n);
// Space complexity: O(n);
