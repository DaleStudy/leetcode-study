/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * 시간복잡도 계산
 * 입력 크기(n)가 커질 때 연산 횟수가 n^2에 비례해서 증가
 * => O(n^2)
 * 
 * 공간복잡도 계산
 * 상수 i 할당
 * 상수 j 할당
 * => o(1)
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (i === j) continue;
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * 시간복잡도 계산
 * 입력 크기(n)가 커질 때 연산 횟수가 n에 비례해서 증가
 * => O(n)
 * 
 * 공간복잡도 계산
 * result가 nums에 비례해서 할당
 * 상수 i, findNum 할당
 * => O(n)
 */
var twoSum = function (nums, target) {
  let result = {};

  nums.forEach((num, index) => {
    result[num] = index;
  });

  for (let i = 0; i < nums.length; i++) {
    const findNum = target - nums[i];

    if (findNum in result && result[findNum] !== i) {
      return [i, result[findNum]];
    }
  }
};
