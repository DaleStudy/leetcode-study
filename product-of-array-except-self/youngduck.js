/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const numsLength = nums.length;

  const result = new Array(numsLength).fill(1);

  // for문 하나로 처리할경우 O(n^2).
  // for문 두개로 나눠서 처리할경우 O(n). 누적곱 개념을 활용해줘야함

  let left = 1;
  let right = 1;

  for (let i = 0; i < numsLength; i++) {
    result[i] *= left;
    left *= nums[i];

    result[numsLength - i - 1] *= right;
    right *= nums[numsLength - i - 1];
  }

  // 시간복잡도: O(n), 공간복잡도: O(1)

  return result;
};
