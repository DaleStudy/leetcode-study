/**
 * 풀이
 * 1. prefix는 현재 인덱스까지의 곱을 저장하고, suffix는 현재 인덱스 이후의 곱을 저장한다.
 * 2. 첫 번째 반복문에서 prefix를 계산하고, 두 번째 반복문에서 suffix를 계산하여 answer 배열에 곱한다.
 * 시간 복잡도 - O(n) : 배열을 두 번 순회
 * 공간 복잡도 - O(1) : answer 배열
 *
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let prefix = 1;
  let suffix = 1;
  const n = nums.length;
  let answer = new Array(n).fill(1);

  // 순방향
  for (let i = 0; i < n; i++) {
    answer[i] = prefix;
    prefix *= nums[i];
  }

  // 역방향
  for (let i = n - 1; i >= 0; i--) {
    answer[i] *= suffix;
    suffix *= nums[i];
  }
  return answer;
};
