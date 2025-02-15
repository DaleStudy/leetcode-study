/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    const pivotIndex = findPivot(nums);

    const firstHalfResult = findIndex(nums, 0, pivotIndex - 1, target);

    return firstHalfResult === -1 ? findIndex(nums, pivotIndex, nums.length - 1, target) : firstHalfResult;
};

function findIndex(nums, start, end, target) {
    while (start <= end) {
        // console.log(start, end, target)
        const mid = start + Math.floor((end - start) / 2);

        const midValue = nums[mid];

        if (midValue === target) {
            return mid;
        }

        if (nums[start] === target) {
            return start;
        }

        if (nums[end] === target) {
            return end;
        }

        if (nums[mid] < target) {
            start = mid + 1;
        } else if (nums[mid] > target) {
            end = mid - 1;
        }
    }

    return -1;
}


function findPivot(nums) {
    let low = 0;
    let high = nums.length - 1;

    while (low <= high) {
        const mid = low + Math.floor((high - low) / 2);

        if (0 < mid && nums[mid - 1] > nums[mid]) {
            return mid;
        }

        if (nums[0] <= nums[mid]) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }

    }

    return 0;
}

// 시간복잡도 O(logn) -> 피봇, 최소값을 찾을 때 이진탐색을 사용하므로
// 공간복잡도 O(1) -> 고정된 변수 사용 이외에는 동적인 배열, 객체를 사용하지 않으므로
