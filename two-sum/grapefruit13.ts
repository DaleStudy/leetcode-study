/**
 * @description nums 배열에서 두 수를 더해 target을 만족하는 인덱스를 반환
 * @param {number[]} nums - 숫자 배열
 * @param {number} target - 목표 숫자
 * @return {number[]} - 두 수의 인덱스
 */
var twoSum = function (nums, target) {
  const map = new Map();

  for (let i = 0; i < nums.length; i++) {
    const current = nums[i];
    const needed = target - current;
    if (map.has(needed)) {
      return [map.get(needed), i];
    }
    map.set(current, i);
  }
};
