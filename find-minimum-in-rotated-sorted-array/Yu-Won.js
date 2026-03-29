/**
 * @param {number[]} nums
 * @return {number}
 *
 * 문제: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 * 요구사항: 이진트리 활용
 */
const findMin = (nums) => {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return nums[left];
};