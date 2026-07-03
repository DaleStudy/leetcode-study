/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const numsSet = new Set(nums);
  return numsSet.size !== nums.length;
};

/*
TC: O(n) -> nums 개수 만큼
SC: O(n) -> 중복 삭제 후 요소 수 만큼 메모리 사용
*/
