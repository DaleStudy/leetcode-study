/**
 * 문제: 배열에서 자신을 제외한 모든 원소의 곱을 구하는 함수 구하기
 * 제약조건: 나눗셈 사용하지 않고, O(n) 시간 복잡도로 풀어야 함
 *
 * Brute Force 방법으로는 각 원소에 대해 나머지 원소들의 곱을 구하는 방법이 있지만,
 * 이는 O(n^2) 시간 복잡도를 가지므로 제약조건에 어긋남
 *
 * O(n) 시간 복잡도로 해결하기 위해서는,
 * 두 번의 순회를 통해 각 원소의 왼쪽과 오른쪽 곱을 따로 계산한 후,
 * 최종적으로 두 곱을 곱해주는 방법을 사용할 수 있음
 *
 * 이 방법은 추가적인 공간을 사용하지 않고,
 * 결과를 저장하는 배열을 사용하여 각 원소의 왼쪽 곱을 저장한 후
 * 오른쪽 곱을 계산하여 결과 배열에 곱해주는 방식으로 구현됨
 *
 * 접근방법:
 * 1. 왼쪽에서 오른쪽으로 누적 곱을 계산 (prefix 곱).
 * 2. 오른쪽에서 왼쪽으로 누적 곱을 계산 (suffix 곱).
 * 3. 각 위치 i에 대해 i 위치 이전까지의 prefix 곱과 i 위치 이후의 suffix 곱을 곱하여 결과를 저장
 */

/**
 * @param {number[]} nums - 입력 배열
 * @return {number[]} - 결과 배열 (answer[i]는 nums[i]를 제외한 모든 원소의 곱)
 */
var productExceptSelf = function (nums) {
  const n = nums.length;

  // 최종 리턴 할 결과 배열 초기화 (O(1) 추가 공간을 위해 출력 배열만 사용)
  const result = Array.from({ length: n }, () => 1);

  let leftProduct = 1;
  for (let i = 0; i < n; i++) {
    result[i] = leftProduct; // 현재 위치 이전까지의 누적 곱 저장
    leftProduct *= nums[i]; // 다음 위치를 위해 현재 원소 곱해서 중간결과(result) 업데이트
  }

  let rightProduct = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] *= rightProduct; // 현재 결과에 오른쪽 누적 곱을 곱해줌
    rightProduct *= nums[i]; // 다음 위치를 위해 현재 원소 곱함
  }

  return result;
};
