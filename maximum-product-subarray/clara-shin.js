/**
 * 정수 배열에서 연속된 부분배열(subarray)의 곱이 최대가 되는 값을 찾는 함수
 *
 * 음수끼리 곱하면 양수가 됨
 * 0이 나오면 곱은 0이 됨 => 부분배열을 새로 시작해야 함
 * 최대값과 최소값을 동시에 추적해야 함: 음수의 경우 최대값이 최소값이 될 수 있음
 *
 * 접근 방법: 동적 프로그래밍
 * 시간복잡도: O(n), 공간복잡도: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  if (nums.length === 0) return 0;

  // 현재 위치에서 끝나는 부분배열의 최대곱과 최소곱
  let maxHere = nums[0];
  let minHere = nums[0];
  let result = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];

    // 현재 숫자가 음수라면 max와 min이 바뀔 수 있음
    if (num < 0) {
      [maxHere, minHere] = [minHere, maxHere];
    }

    // 현재 숫자부터 새로 시작하거나, 기존 곱에 현재 숫자를 곱함
    maxHere = Math.max(num, maxHere * num);
    minHere = Math.min(num, minHere * num);

    // 전체 최대값 업데이트
    result = Math.max(result, maxHere);
  }

  return result;
};
