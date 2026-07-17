/**
 * 구간 내 최대 합을 dp에 저장
 * 시간복잡도 O(n)
 * 공간복잡도 O(1)
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let prev = nums[0];
  let max = nums[0];

  for (let i = 1; i < nums.length; i++) {
    prev = Math.max(prev + nums[i], nums[i]);
    max = Math.max(max, prev);
  }

  return max;
};
