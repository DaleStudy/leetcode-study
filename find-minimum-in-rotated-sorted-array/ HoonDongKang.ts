/**
 * [Problem]: [153] Find Minimum in Rotated Sorted Array
 *
 * (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)
 */

function findMin(nums: number[]): number {
    // 실제 Submit은 되나, 문제의 의도와 다름
    function ggomsuFunc(nums: number[]): number {
        return Math.min(...nums);
    }

    //시간복잡도 O(logn)
    //공간복잡도 O(1)
    function binarySearchFunc(nums: number[]): number {
        let left = 0;
        let right = nums.length - 1;

        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }

    return binarySearchFunc(nums);
};
