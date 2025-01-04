/**
 * 시간 복잡도: nums.length + 1만큼 순회하므로 O(n)
 * 공간 복잡도: totalSum, numsSum 변수를 사용하므로 O(1)
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
  const n = nums.length;
  const totalSum = n * (n + 1) / 2;
  let numsSum = 0;
  for(const n of nums) {
      numsSum += n;
  }
  return totalSum - numsSum;
};
