// ✅ Time Complexity: O(n)
// ✅ Space Complexity: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  // Edge case: If there's only one house, return its value
  if (nums.length === 1) return nums[0];

  // helper function
  const robHouses = (start, end) => {
    // prev1: stores the maximum money robbed up to the previous house.
    // prev2: stores the maximum money robbed up to the house before the previous house.
    let prev1 = 0,
      prev2 = 0;

    for (let i = start; i <= end; i++) {
      let temp = Math.max(prev1, prev2 + nums[i]);

      prev2 = prev1;

      prev1 = temp;
    }

    return prev1;
  };

  // Excluding the last house: robHouses(0, nums.length - 2)
  // Excluding the first house: robHouses(1, nums.length - 1)

  return Math.max(robHouses(0, nums.length - 2), robHouses(1, nums.length - 1));
};

