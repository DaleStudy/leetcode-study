/**
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
 * time complexity : O(log n)
 * space complexity : O(1)
 */

function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (nums[mid] > nums[right]) left = mid + 1;
        else right = mid;
    }

    return nums[left];
};
