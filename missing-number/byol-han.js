/**
 * https://leetcode.com/problems/missing-number/
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== i) {
      return i; // 빠진 숫자를 찾으면 리턴
    }
  }

  return nums.length; // 모든 숫자가 다 있으면 빠진 건 n
};

// 수학적 합 공식 이용하기 (가장 빠름)
//시간복잡도: O(n)
// 공간복잡도: O(1) (아주 효율적)

var missingNumber = function (nums) {
  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;
  const actualSum = nums.reduce((a, b) => a + b, 0);
  return expectedSum - actualSum;
};
