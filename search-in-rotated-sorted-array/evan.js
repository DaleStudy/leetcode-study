/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let leftIndex = 0;
  let rightIndex = nums.length - 1;

  while (leftIndex <= rightIndex) {
    const midIndex = Math.floor((rightIndex + leftIndex) / 2);
    const [leftValue, midValue, rightValue] = [
      nums[leftIndex],
      nums[midIndex],
      nums[rightIndex],
    ];

    if (midValue === target) {
      return midIndex;
    }

    if (leftValue <= midValue) {
      if (leftValue <= target && target < midValue) {
        rightIndex = midIndex - 1;
      } else {
        leftIndex = midIndex + 1;
      }
    } else {
      if (midValue < target && target <= rightValue) {
        leftIndex = midIndex + 1;
      } else {
        rightIndex = midIndex - 1;
      }
    }
  }

  return -1;
};
