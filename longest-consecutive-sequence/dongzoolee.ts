function longestConsecutive(nums: number[]): number {
  const st = new Set(nums);

  let mx = 0;
  for (const n of st) {
    if (st.has(n - 1)) continue;

    let len = 1;
    while (st.has(n + len)) {
      len++;
    }

    mx = Math.max(mx, len);
  }

  return mx;
}
