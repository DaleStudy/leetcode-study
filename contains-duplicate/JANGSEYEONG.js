/*
  시간복잡도: O(n) - new Set(nums)에서 배열 요소 순회하며 Set 생성 O(n) + 길이 비교 O(1)
  - Set 자료구조는 중복된 값을 자동으로 제거
*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // Set으로 만들었을 때, 기존 배열과 사이즈가 다르면 중복이 제거된거임
  const numsSet = new Set(nums);
  return nums.length !== numsSet.size;
};
