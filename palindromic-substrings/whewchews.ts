function countSubstrings(s: string): number {
  // SC: O(N^2)
  const dict: Map<string, boolean> = new Map();
  const n = s.length;

  // TC: O(N^2)
  for (let start = n; start >= 0; start--) {
    for (let end = start; end < n; end++) {
      if (start === end) {
        dict.set(`${start}:${end}`, true);
      } else if (start + 1 === end) {
        dict.set(`${start}:${end}`, s[start] === s[end]);
      } else {
        const flag = s[start] === s[end];
        const mid = dict.get(`${start + 1}:${end - 1}`);
        dict.set(`${start}:${end}`, flag && mid);
      }
    }
  }

  let cnt = 0;

  // TC: O(N^2)
  // SC: O(1)
  for (const v of dict.values()) {
    if (v) {
      cnt++;
    }
  }

  return cnt;
}

// TC: O(N^2)
// SC: O(N^2)
