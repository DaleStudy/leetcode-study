var threeSum = function (nums) {
  // Sort nums array
  const sortedNums = nums.sort((a, b) => a - b);
  let result = [];

  // Start iteration to pick first element for 3sum
  for (let i = 0; i < sortedNums.length; i++) {
    // Check if the first element is already greater than 0, no valid triplets possible after this point
    if (sortedNums[i] > 0) {
      break;
    }

    // Skip duplicates of the first element to avoid redundant triplets
    if (i > 0 && sortedNums[i] === sortedNums[i - 1]) {
      continue;
    }

    // Iterate to find sum of two pointer and nums[i]
    let left = i + 1;
    let right = sortedNums.length - 1;

    while (left < right) {
      let sum = sortedNums[i] + sortedNums[left] + sortedNums[right];

      if (sum === 0) {
        result.push([sortedNums[i], sortedNums[left], sortedNums[right]]);
        // Skip duplicates of left and right pointers to avoid redundant triplets
        while (sortedNums[left] === sortedNums[left + 1]) left++;
        while (sortedNums[right] === sortedNums[right - 1]) right--;
        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else if (sum > 0) {
        right--;
      }
    }
  }
  return result;
};

// TC: O(n^2)
// SC: O(n)
