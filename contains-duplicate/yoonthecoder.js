var containsDuplicate = function (nums) {
  // Create a set from the nums array. Since Sets only allow unique values, any duplicates will be removed.
  const set = new Set(nums);
  // Compare the size of the set and the length of the original array.- if the size of the set is smaller than the length of the original array('nums'), it means there were duplicates.

  return set.size < nums.length;
};

// Time Complexity: O(n); - adding elements to the Set & compare sizes
// Space Complexity: O(n)
