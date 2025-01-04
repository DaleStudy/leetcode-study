/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  // 1. nums 정렬
  nums.sort((a, b) => a - b);
  // 2. for문 돌며 빠진 숫자 찾기
  for (let i = 0; i <= nums.length; i++) {
    if (nums[i] !== i) {
      return i;
    }
  }
};

// 시간 복잡도: O(nlogn)
// 공간 복잡도: O(1)
