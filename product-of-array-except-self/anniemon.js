/**
 * 시간 복잡도: nums의 길이를 상수 크기만큼 순회하므로 O(n)
 * 공간 복잡도: nums의 길이에 상수 크기만큼 비례하므로 O(n)
 */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  let prefix = Array(nums.length+1).fill(1);
  let suffix = Array(nums.length+1).fill(1);
  for(let i=0; i <nums.length; i++) {
      prefix[i+1] = nums[i] * prefix[i];
      suffix[nums.length-i-1] = suffix[nums.length-i] * nums[nums.length - i-1];
  }
  for(let i=0; i <nums.length; i++) {
      nums[i] = prefix[i] * suffix[i+1];
  }
  return nums;
};
