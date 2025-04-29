/**
 * 주어진 배열의 최솟값을 반환하는 함수
 * @param {number[]} nums
 * @return {number}
 */
// 첫 번째 시도
const findMin = function(nums) {
    return Math.min(...nums);
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)

// ===========================================
// 두 번째 시도
const findMin = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    let mid;

    while (left < right) {
        mid = Math.floor((left + right) / 2);

        if (nums[mid] < nums[right]) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return nums[left];
}

// 시간복잡도: O(logn)
// 공간복잡도: O(1)
