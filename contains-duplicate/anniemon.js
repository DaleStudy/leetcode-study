/**
 * 시간 복잡도:
 * 맵에서 nums[i]를 찾거나 삽입하는 데 걸리는 시간 O(1) * n(nums.length)
 * 즉, O(n)
 * 공간 복잡도:
 * 최대 map의 크기는 nums.length만큼
 * 즉, O(n)
 */
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  const map = new Map();
  for(let i = 0; i < nums.length; i++) {
      if(!map.has(nums[i])) {
          map.set(nums[i], i);
      } else {
          return true;
      }
  }
  return false;
};
