/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        // 중간값이 오른쪽보다 크면 최소값은 오른쪽에 있다!
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            // 최소값은 mid를 포함한 왼쪽에 있다!
            right = mid;
        }
    }

    // left == right일 때 최소값이 위치함
    return nums[left];
};

// 시간 복잡도: O(log n), 이진 탐색으로 탐색 범위를 절반씩 줄여나감
// 공간 복잡도: O(1), 추가적인 공간을 사용하지 않음
