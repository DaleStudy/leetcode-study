/**
 * 125. Valid Palindrome
 * A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
 * non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
 * and numbers.
 * Given a string s, return true if it is a palindrome, or false otherwise.
 * https://leetcode.com/problems/valid-palindrome/description/
 */
function isPalindrome(s: string): boolean {
  const chars = s.replace(/[^a-z0-9]/gi, "").toLowerCase();

  return chars === [...chars].reverse().join("");
}

// O(n) time
// O(n) space
