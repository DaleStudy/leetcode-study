/**
 * @description - 같은 날 인접한 두 집에 침입 시 자동으로 신고됨
 * @param nums - 각 집의 금액을 나타내는 정수 배열
 * @returns - 경찰에 신고되지 않고 훔칠 수 있는 최대 금액
 *
 * @description
 * - 1. tabulation 방식 - O(n)
 */
// function rob(nums: number[]): number {
//   if (nums.length < 2) {
//     return nums[0];
//   }

//   const dpTable: Array<number> = Array.from({ length: nums.length }, () => 0);
//   dpTable[0] = nums[0];
//   dpTable[1] = Math.max(nums[0], nums[1]);

//   for (let i = 2; i < nums.length; i++) {
//     dpTable[i] = Math.max(nums[i] + dpTable[i - 2], dpTable[i - 1]);
//   }

//   return Math.max(...dpTable);
// }

function rob(nums: number[]): number {
  const memo: Array<number> = Array.from({ length: nums.length }, () => -1);

  function solve(i: number): number {
    if (i < 0) {
      return 0;
    }

    if (memo[i] !== -1) {
      return memo[i];
    }

    const robCurrent = nums[i] + solve(i - 2);
    const skipCurrent = solve(i - 1);
    memo[i] = Math.max(robCurrent, skipCurrent);
    return memo[i];
  }
  return solve(nums.length - 1);
}
