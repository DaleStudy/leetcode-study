/**
 * [Problem]: [33] Search in Rotated Sorted Array
 * (https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
 */
function search(nums: number[], target: number): number {
    //시간복잡도 O(log n)
    //공간복잡도 O(1)
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) return mid;

        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
}
