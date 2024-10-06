/**
 * https://leetcode.com/problems/longest-repeating-character-replacement
 * T.C. O(n)
 * S.C. O(1)
 */
function characterReplacement(s: string, k: number): number {
  const charCount = new Array(26).fill(0);
  let maxCount = 0;
  let start = 0;
  let maxLen = 0;

  const A = 'A'.charCodeAt(0);
  for (let end = 0; end < s.length; end++) {
    const endCharIdx = s.charCodeAt(end) - A;
    maxCount = Math.max(maxCount, ++charCount[endCharIdx]);

    if (end - start + 1 - maxCount > k) {
      charCount[s.charCodeAt(start) - A]--;
      start++;
    }

    maxLen = Math.max(maxLen, end - start + 1);
  }
  return maxLen;
}
