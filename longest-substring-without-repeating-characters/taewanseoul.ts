/**
 * 3. Longest Substring Without Repeating Characters
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 */

// O(n^2) time
// O(n) space
function lengthOfLongestSubstring(s: string): number {
  let result = 0;

  for (let i = 0; i < s.length; i++) {
    let set = new Set();
    let substring = 0;

    for (let j = i; j < s.length; j++) {
      if (set.has(s[j])) {
        break;
      }

      set.add(s[j]);
      substring++;
    }

    result = Math.max(result, substring);
  }

  return result;
}
