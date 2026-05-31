/**
 * @param nums - 정수 배열
 * @returns - 정수 배열의 부분 배열의 곱이 가장 큰 값을 반환
 * @description
 * - 값이 음수일 경우 최솟값과 곱해 최댓값을 도출 할 수 있으므로 swap
 * - min, max를 현재 값과 비교하며 변경
 */

function maxProduct(nums: number[]): number {
  let maximum = nums[0];
  let minimum = nums[0];
  let result = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const current = nums[i];

    if (current < 0) {
      let temp = maximum;
      maximum = minimum;
      minimum = temp;
    }

    maximum = Math.max(current, current * maximum);
    minimum = Math.min(current, current * minimum);

    result = Math.max(result, maximum);
  }

  return result;
}

const nums = [-2, 3, -4];

maxProduct(nums);



