// 좌->우 방향의 누적곱과 우->좌 방향의 누적곱 활용
// TC: O(N)
// SC: O(N) (답안을 제외하면 O(1))

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const result = new Array(nums.length).fill(1);

  let leftToRight = 1;
  for (let index = 1; index < nums.length; index++) {
    leftToRight *= nums[index - 1];
    result[index] *= leftToRight;
  }

  let rightToLeft = 1;
  for (let index = nums.length - 2; index >= 0; index--) {
    rightToLeft *= nums[index + 1];
    result[index] *= rightToLeft;
  }

  return result;
};

// 1차 풀이
// 0의 갯수가 0개, 1개, 2개인 경우로 나눠서 풀이
// 0개인 경우, 답안 배열의 원소는 '모든 원소 곱 / 현재 원소'
// 1개인 경우, 0의 위치한 원소만 '0을 제외한 모든 원소 곱' 이고 그 외 '0'
// 2개인 경우, 답안 배열의 모든 원소가 '0'

// TC: O(N)
// SC: O(N)

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const zeroCount = nums.filter((num) => num === 0).length;
  if (zeroCount > 1) {
    return new Array(nums.length).fill(0);
  }

  const multipled = nums.reduce(
    (total, current) => (current === 0 ? total : total * current),
    1
  );

  if (zeroCount === 1) {
    const zeroIndex = nums.findIndex((num) => num === 0);
    const result = new Array(nums.length).fill(0);
    result[zeroIndex] = multipled;
    return result;
  }

  return nums.map((num) => multipled / num);
};
