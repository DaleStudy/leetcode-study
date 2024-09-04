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
// nums 정렬을 하기 위해서 순회 (길이 n)
// 빠진 숫자를 찾기위해서 순회 (최대길이 n)
// O(2n) 따라서 시간 복잡도는 O(n)

// SC
// 길이가 n인 배열을 저장할 공간 필요
// O(n)
