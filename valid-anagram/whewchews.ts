function isAnagram(s: string, t: string): boolean {
  // TC: O(1)
  if (s.length !== t.length) return false;

  // SC: O(N)
  const count: { [key: string]: number } = {};

  // TC: O(N)
  for (let i = 0; i <= s.length - 1; i++) {
    const sChar = s[i];
    const tChar = t[i];
    count[sChar] = (count[sChar] || 0) + 1;
    count[tChar] = (count[tChar] || 0) - 1;
  }

  // TC: O(N)
  return Object.values(count).every((v) => v === 0);
}

// TC: O(N)
// SC: O(N)
