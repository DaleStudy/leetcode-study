/**
 * @param nums - 정수 배열
 * @returns - nums[i]를 제외한 요소들의 곱셈 값 배열
 * @description
 * - 나누기를 통한 풀이는 막힘
 * - 왼쪽, 오른쪽으로 순회하며 곱을 누적하기
 * - 첫번째 반복 - 처음 값은 자신을 제외한 누적의 전체이므로 1, 이후 부터 누적
 * - 두번째 반복 - 마지막 값 또한 자신을 제외한 첫번째 반복의 누적, 이후 부터 미리 누적한 값과 자신을 곱
 *
 * @description
 * - 시간 복잡도 O(n)
 * - 공간 복잡도 O(n)
 * - 해당 방법을 떠올리지 못해 AI의 도움을 받았는데 수학적 사고가 더 필요하다.
 */
function productExceptSelf(nums: number[]): number[] {
  let prev = 1;
  let next = 1;
  const arr: number[] = [];

  for (let i = 0; i < nums.length; i++) {
    arr.push(prev);
    prev = prev * nums[i];
  }

  for (let j = nums.length - 1; j >= 0; j--) {
    arr[j] = arr[j] * next;
    next = next * nums[j];
  }

  return arr;
}

const nums = [1, 2, 3, 4];
productExceptSelf(nums);
