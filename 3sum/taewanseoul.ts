/**
 * 15. 3Sum
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 * Notice that the solution set must not contain duplicate triplets.
 *
 * https://leetcode.com/problems/3sum/description/
 */
function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);
  const triplets: number[][] = [];

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0 || nums[i] === nums[i - 1]) {
      continue;
    }

    let low = i + 1;
    let high = nums.length - 1;

    while (low < high) {
      const sum = nums[i] + nums[low] + nums[high];
      if (sum < 0) {
        low++;
      } else if (sum > 0) {
        high--;
      } else {
        triplets.push([nums[i], nums[low], nums[high]]);

        while (low < high && nums[low] === nums[low + 1]) {
          low++;
        }
        while (low < high && nums[high] === nums[high - 1]) {
          high--;
        }
        low++;
        high--;
      }
    }
  }

  return triplets;
}

// O(n^2) time
// O(n) space
