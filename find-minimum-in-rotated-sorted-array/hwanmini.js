// 시간복잡도: O(log n)
// 공간복잡도: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let leftIdx = 0;
    let rightIdx = nums.length - 1;

    if (nums.length === 1) return nums[0]

    while (leftIdx <= rightIdx) {
        if (nums[leftIdx] < nums[rightIdx]) return nums[leftIdx]

        let midIdx = Math.floor((leftIdx + rightIdx) / 2);

        if (nums[midIdx] > nums[midIdx+1]) {
            return nums[midIdx+1]
        }

        if (nums[leftIdx] < nums[midIdx] && nums[leftIdx] > nums[rightIdx]) {
            leftIdx = midIdx
        } else {
            rightIdx = midIdx
        }
    }

    return nums[0]
};

