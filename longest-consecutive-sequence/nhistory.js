var longestConsecutive = function (nums) {
  // Return 0 if there are no elements in nums
  if (nums.length === 0) return 0;

  // Create a set to find values efficiently
  const numSet = new Set(nums);
  let maxLength = 0;

  for (let num of numSet) {
    // Check if this is the start of a sequence
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;

      // Count the length of the sequence
      while (numSet.has(currentNum + 1)) {
        currentNum += 1;
        currentLength += 1;
      }

      // Update the maximum length
      maxLength = Math.max(maxLength, currentLength);
    }
  }

  return maxLength;
};

// TC: O(n)
// SC: O(n)
