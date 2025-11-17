// Time Complexity: O(n)
// Space Complexity: O(1)
function rob(nums: number[]): number {
  const n = nums.length;

  if (n === 1) return nums[0];
  if (n === 2) return Math.max(nums[0], nums[1]);

  const getLinearRob = (start: number, end: number) => {
    let prev2 = 0;
    let prev1 = 0;

    for (let i = start; i <= end; i++) {
      const current = Math.max(prev1, prev2 + nums[i]);
      prev2 = prev1;
      prev1 = current;
    }

    return prev1;
  };

  let case1 = getLinearRob(0, n - 2);
  let case2 = getLinearRob(1, n - 1);

  return Math.max(case1, case2);
}
