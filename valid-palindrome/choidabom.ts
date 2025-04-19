// https://leetcode.com/problems/valid-palindrome/

// TC: O(n)
// SC: O(n)

function isPalindrome(s: string): boolean {
  const str = (s.toLowerCase().match(/[a-z0-9]/g) || []).join("");
  const reverse = str.split("").reverse().join("");

  return str === reverse;
}
