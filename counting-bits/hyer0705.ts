// Time Complexity: O(n)
// Space Complexity: O(n)
function countBits(n: number): number[] {
  const ans: number[] = Array.from({ length: n + 1 }, () => 0);

  for (let i = 1; i <= n; i++) {
    ans[i] = ans[i >> 1] + (i & 1);
  }

  return ans;
}
