/**
 * https://leetcode.com/problems/longest-palindromic-substring
 * T.C. O(n^2)
 * S.C. O(1)
 */
function longestPalindrome(s: string): string {
  if (s.length < 2) return s;
  let start = 0;
  let end = 0;

  for (let i = 0; i < s.length; i++) {
    const len1 = expandBothSides(s, i, i); // odd
    const len2 = expandBothSides(s, i, i + 1); // even
    const len = Math.max(len1, len2);

    if (len > end - start) {
      start = i - Math.floor((len - 1) / 2);
      end = i + Math.floor(len / 2);
    }
  }

  return s.slice(start, end + 1);
}

function expandBothSides(s: string, left: number, right: number): number {
  while (0 <= left && right < s.length && s[left] === s[right]) {
    left--;
    right++;
  }

  return right - left - 1;
}
