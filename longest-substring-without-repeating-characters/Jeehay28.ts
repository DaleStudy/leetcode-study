// TC: O(n)
// SC: O(n)

function lengthOfLongestSubstring(s: string): number {
  let seen = new Map<string, number>();
  let maxLength = 0;
  let start = 0;

  for (let end = 0; end < s.length; end++) {
    const ch = s[end];

    if (seen.has(ch) && seen.get(ch)! >= start) {
      start = seen.get(ch)! + 1;
    }

    seen.set(ch, end);
    maxLength = Math.max(maxLength, end - start + 1);
  }

  return maxLength;
}
