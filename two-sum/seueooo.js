/**
풀이
해시맵으로 값의 존재 여부 확인 -> O(1)
배열을 딱 한번 순회하므로 O(n).
 */
var twoSum = function (nums, target) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const num = target - nums[i];
    if (map.has(num)) {
      return [map.get(num), i];
    }
    map.set(nums[i], i);
  }
  return [];
};
