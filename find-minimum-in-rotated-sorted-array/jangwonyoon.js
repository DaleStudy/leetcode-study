/**
 * 153. Find Minimum in Rotated Sorted Array
 *  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 *
 */

/**
 * 풀이 1
 * 정렬 Sorting
 *
 * @param {number[]} nums
 * @return {number}
 *
 * 시간 복잡도(TC): O(n log n)
 * 공간 복잡도(SC): O(1)
 *
 * 관련 알고리즘: 정렬 Sorting
 *
 * 문제 풀이 방법:
 * 1. 배열을 정렬하고 첫 번째 요소를 반환
 *
 * 문제의 의도와 맞지 않는듯
 */

var findMin = function(nums) {
    return nums.sort((a, b) => a - b)[0];
};

/**
 * 풀이 2
 * 투 포인터 Two Pointers
 *
 * @param {number[]} nums
 * @return {number}
 *
 * 시간 복잡도(TC): O(n)
 * 공간 복잡도(SC): O(1)
 *
 * 관련 알고리즘: 투 포인터 Two Pointers
 *
 * 문제 풀이 방법:
 * 1. 배열을 순회하면서 최소값을 찾으면 된다.
 * 2. 최소값을 찾으면 반환
 */

var findMin = function(nums) {
    let result = Infinity;

    for (let i = 0; i < nums.length; i++) {
        const curr = nums[i];
        result = Math.min(result, curr);
    }

    return result;
};

/**
 * 풀이 3
 * 이진 탐색 Binary Search
 *
 * @param {number[]} nums
 * @return {number}
 *
 * 시간 복잡도(TC): O(log n)
 * 공간 복잡도(SC): O(1)
 *
 * 관련 알고리즘: 이진 탐색 Binary Search
 *
 * 문제 풀이 방법:
 * 1. 배열을 이진 탐색으로 탐색
 */

var findMin = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        // mid가 right보다 크면 최소값은 오른쪽
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            // mid가 right보다 작다면
            right = mid;
        }
    }

    return nums[left];
};
