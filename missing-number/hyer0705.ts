// Time Complexity: O(n)
// Space Complexity: O(1)
function missingNumber(nums: number[]): number {
  const n = nums.length;

  const expectedSum = (n * (n + 1)) / 2;
  const currentSum = nums.reduce((acc, curr) => acc + curr, 0);

  return expectedSum - currentSum;
}

// Time Complexity: O(n^2)
// Space Complexity: O(1)
function missingNumber(nums: number[]): number {
  const n = nums.length;

  for (let i = 0; i <= n; i++) {
    if (!nums.includes(i)) return i;
  }

  return -1;
}
