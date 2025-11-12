/**
 * 가장 단순한 O(n^2) 로 풀이하였습니다
 */
function twoSum(nums: number[], target: number): number[] {
  let temp_i = 0;
  let temp_j = 0;

  for (let i = 0; i < nums.length; i++) {
    temp_i = nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      temp_j = nums[j];

      if (temp_i + temp_j === target) {
        return [i, j];
      }
    }
  }

  return [];
}
