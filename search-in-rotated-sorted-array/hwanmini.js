// 시간복잡도: O(log n)
// 공간복잡도: O(1)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let leftIdx = 0;
    let rightIdx = nums.length - 1;

    while (leftIdx <= rightIdx) {
        const midIdx = Math.floor((leftIdx + rightIdx) / 2);

        if (nums[midIdx] === target) return midIdx;

        if (nums[leftIdx] <= nums[midIdx]) {
            if (nums[leftIdx] <= target && nums[midIdx] >= target) {
                rightIdx = midIdx - 1;
            } else {
                leftIdx = midIdx + 1;
            }
        } else {
            if (nums[rightIdx] >= target && nums[midIdx] <= target) {
                leftIdx = midIdx + 1;
            } else {
                rightIdx = midIdx - 1;
            }
        }
    }

    return -1
};
