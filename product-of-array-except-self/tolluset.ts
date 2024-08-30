/*
 * TC: O(n)
 * SC: O(n)
 * */

function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const answer = new Array(n).fill(1);

  let left = 1;
  nums.forEach((num, i) => {
    answer[i] = left;
    left *= num;
  });

  let right = 1;
  nums.reverse().forEach((num, i) => {
    answer[n - 1 - i] *= right;
    right *= num;
  });

  return answer;
}
