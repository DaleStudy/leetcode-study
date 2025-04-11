/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  // 1.
  // 각 인덱스에서 자기 자신 제외한 배열 만든 뒤 곱셈 수행 → 시간복잡도 O(n²)
  // (중첩 루프로 인해 시간복잡도 O(n²), 큰 입력에서는 시간 초과 발생)
  let result = [];
  for (let i = 0; i < nums.length; i++) {
    const productNums = [...nums.slice(0, i), ...nums.slice(i + 1)];

    let product = 1;
    for (let j = 0; j < productNums.length; j++) {
      product *= productNums[j];
    }
    result.push(product);
  }
  return result;

  // 2.
  const n = nums.length;
  // 정답 배열을 1로 초기화 (곱셈에 영향을 주지 않도록)
  const answer = new Array(n).fill(1);

  // 왼쪽 누적 곱 계산
  let left = 1;
  for (let i = 0; i < n; i++) {
    answer[i] = left;
    left *= nums[i];
  }

  // 오른쪽 누적 곱 계산
  let right = 1;
  for (let i = n - 1; i >= 0; i--) {
    answer[i] *= right;
    right *= nums[i];
  }

  return answer;
};
