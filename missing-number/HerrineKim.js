// 시간 복잡도: O(n)
// 공간 복잡도: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
  const n = nums.length;
  // 0부터 n까지의 합 공식: n * (n + 1) / 2
  const expectedSum = (n * (n + 1)) / 2;
  // 실제 배열의 합
  const actualSum = nums.reduce((sum, num) => sum + num, 0);
  
  return expectedSum - actualSum;
};

