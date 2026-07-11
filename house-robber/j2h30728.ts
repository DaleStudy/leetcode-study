/**
 *
 * @param nums
 * @returns
 * 시간 복잡도 : O(n)
 * 공간 복잡도 : O(n)
 */
function rob(nums: number[]): number {
  const memo = new Map<number, number>();
  return recursive(nums, nums.length - 1, memo);
}

function recursive(nums: number[], index: number, memo: Map<number, number>) {
  if (index < 0) {
    return 0;
  }

  if (memo.has(index)) {
    return memo.get(index);
  }

  const result = Math.max(
    recursive(nums, index - 2, memo) + nums[index],
    recursive(nums, index - 1, memo),
  );
  memo.set(index, result);

  return result;
}

/**
 *
 * @param nums
 * @returns
 * 시간 복잡도 : O(n)
 * 공간 복잡도 : O(1)
 */
function rob(nums: number[]): number {
  let prev1 = 0;
  let prev2 = 0;

  for (let num of nums) {
    const current = Math.max(prev2 + num, prev1);
    prev2 = prev1;
    prev1 = current;
  }

  return prev1;
}
