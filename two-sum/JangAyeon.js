/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// 첫번째 통과 풀이 - 브루트포스
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        return [i, j];
      }
    }
  }
};

// 두번째 통과 풀이 - 해시맵 + 효율성 고려
var twoSum = function (nums, target) {
  const map = new Map(); // {값: 인덱스}

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i]; // 필요한 짝 계산
    if (map.has(complement)) {
      return [map.get(complement), i]; // 이전에 complement가 있었으면 바로 반환
    }
    map.set(nums[i], i);
  }
};
