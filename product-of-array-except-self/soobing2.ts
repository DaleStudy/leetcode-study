/**
 * 문제 유형
 * - Array
 *
 * 문제 설명
 * - 자기 자신을 제외한 나머지의 곱 구하기
 *
 * 아이디어
 * 1) Array - 자기 자신보다 이전, 이후 의 누적곱(left, right) 구하고, 최종적으로 곱하기
 * 2) 0읠 제외한 나머지의 곱, 0의 갯수 카운트를 이용하여 조건에 따라 계산하기
 */
function productExceptSelf(nums: number[]): number[] {
  const answer = Array(nums.length).fill(0);
  let zeroCount = 0;
  const productWithoutZero = nums.reduce((acc, cur) => {
    if (cur === 0) {
      zeroCount++;
      return acc;
    }
    return cur * acc;
  }, 1);

  for (let i = 0; i < nums.length; i++) {
    if (zeroCount > 0) {
      if (nums[i]) answer[i] = 0;
      else answer[i] = zeroCount > 1 ? 0 : productWithoutZero;
    } else {
      answer[i] = productWithoutZero / nums[i];
    }
  }
  return answer;
}

function productExceptSelfArrayVersion(nums: number[]): number[] {
  const answer = Array(nums.length);
  const left = Array(nums.length).fill(1);
  const right = Array(nums.length).fill(1);

  for (let i = 1; i < nums.length; i++) {
    left[i] = left[i - 1] * nums[i - 1];
  }

  for (let i = nums.length - 2; i >= 0; i--) {
    right[i] = right[i + 1] * nums[i + 1];
  }

  for (let i = 0; i < nums.length; i++) {
    answer[i] = left[i] * right[i];
  }

  return answer;
}
