/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  // 최대 곱을 저장할 변수
  let maxProduct = nums[0];
  // 현재 위치까지의 최대 곱과 최소 곱을 저장할 변수
  let currentMax = nums[0];
  let currentMin = nums[0];

  // 배열의 두 번째 원소부터 순회
  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];

    // 음수를 곱할 경우 최대와 최소가 바뀔 수 있으므로 미리 저장
    const tempMax = currentMax;

    // 현재 숫자와 곱했을 때의 최대/최소 값을 계산
    currentMax = Math.max(num, num * currentMax, num * currentMin);
    currentMin = Math.min(num, num * tempMax, num * currentMin);

    // 전체 최대 곱을 업데이트
    maxProduct = Math.max(maxProduct, currentMax);
  }

  return maxProduct;
};
