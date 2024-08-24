function countBits(n: number): number[] {
  // SC: O(N)
  const ans = Array(n + 1).fill(0);
  // TC: O(N)
  for (let i = 1; i <= n; i++) {
    let k = i;

    // TC: O(log N)
    while (k > 0) {
      ans[i] += k % 2;
      k = Math.floor(k / 2);
    }
  }

  return ans;
}

// TC: O(N log N)
// SC: O(N)
