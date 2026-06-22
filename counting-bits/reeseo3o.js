// Time Complexity: O(n)
// Space Complexity: O(n)

const countBits = (n) => {
  const ans = new Array(n + 1).fill(0);

  for (let i = 1; i <= n; i++) {
    ans[i] = ans[i >> 1] + (i & 1);
  }

  return ans;
};
