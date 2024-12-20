var longestConsecutive = function (nums) {
  // remove the duplicates from the array and sort it in an ascending order.
  const setArray = [...new Set(nums)];
  const sortedArray = setArray.sort((a, b) => a - b);
  // create a set to store streak lengths, even when count resets.
  const countSet = new Set();
  let count = 0;
  for (let i = 0; i < sortedArray.length; i++) {
    if (sortedArray[i] + 1 == sortedArray[i + 1]) {
      count += 1;
      countSet.add(count);
    } else {
      count = 0;
    }
  }

  return nums.length === 0 ? 0 : countSet.size + 1;
};

// Time complexity: O(nlogn) => TODO: need to improve this to O(n)
// Space complexity: O(n)
