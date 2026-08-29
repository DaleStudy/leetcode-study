/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
function isPalindrome(s: string): boolean {
  let string = "";
  for (const ch of s) {
    if (/[a-zA-Z0-9]/.test(ch)) {
      string += ch.toLowerCase();
    }
  }

  for (let i = 0; i < string.length / 2; i++) {
    if (string[i] !== string[string.length - i - 1]) {
      return false;
    }
  }
  return true;
}
