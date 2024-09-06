/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
    nums = nums.sort();

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== i) return i;
    }

    return nums.length;
};

// TC
// nums 정렬을 하기 위해서 순회 (길이 n) -> 최선의 경우 O(n) 이지만, 평균적으로 O(n log n)
// 빠진 숫자를 찾기위해서 순회 (최대길이 n)
// 따라서 시간 복잡도는 최대 O(n log n)

// SC
// 길이가 n인 배열을 저장할 공간 필요
// O(n)
