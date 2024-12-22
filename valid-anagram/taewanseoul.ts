/**
 * 242. Valid Anagram
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 *
 * https://leetcode.com/problems/valid-anagram/description/
 */
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  const charMap = new Map<string, number>();

  for (const char of s) {
    const count = charMap.get(char);
    if (count) {
      charMap.set(char, count + 1);
    } else {
      charMap.set(char, 1);
    }
  }

  for (const char of t) {
    const count = charMap.get(char);
    if (count) {
      charMap.set(char, count - 1);
    } else {
      return false;
    }
  }

  return true;
}

// O(n) time
// O(n) space
