/**
 * @param {number[]} nums
 * @return {boolean}
 * 
 * 시간복잡도 계산
 * 입력 크기(n)가 커질 때 연산 횟수가 n에 비례해서 증가
 * => O(n)
 * 
 * 공간복잡도 계산
 * indices가 nums에 비례해서 할당
 * 상수 i 할당
 * => O(n)
 */
var containsDuplicate = function (nums) {
  let indices = {};
  nums.forEach((num, index) => {
    indices[num] = index;
  });

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in indices && indices[nums[i]] !== i) return true;
  }

  return false;
};

/**
 * @param {number[]} nums
 * @return {boolean}
 * 
 * 시간복잡도 계산
 * Set의 size속성은 입력 크기와 관계없이 일정한 시간이 걸림
 * => O(1)
 * 
 * 공간복잡도 계산
 * indices가 nums에 비례해서 할당
 * 상수 i 할당
 * => O(n)
 */
var containsDuplicate = function (nums) {
  const indices = new Set(nums);

  if (indices.size !== nums.length) return true;

  return false;
};
