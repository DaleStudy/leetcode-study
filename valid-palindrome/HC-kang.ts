/**
 * https://leetcode.com/problems/valid-palindrome/
 * T.C.: O(n)
 * S.C.: O(1)
 */
function isPalindrome(s: string): boolean {
  function isAlNum(char: string): boolean {
    return /^[a-zA-Z0-9]$/.test(char);
  }

  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    while (left < right && !isAlNum(s[left])) left++;
    while (left < right && !isAlNum(s[right])) right--;

    if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      return false;
    }

    left++;
    right--;
  }
  return true;
}
