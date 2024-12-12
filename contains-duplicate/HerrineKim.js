// 시간복잡도: O(n)

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const seen = new Set();
  for (let num of nums) {
    if (seen.has(num)) {
      return true; // 중복 발견
    }
    seen.add(num);
  }
  return false; // 모든 요소가 고유
};