// TC: O(n^2)
// SC: O(1)
function longestPalindrome(s: string): string {
  if (s.length < 2) return s;

  let maxLeft = 0;
  let maxRight = 0;

  const expandWindow = (left: number, right: number): void => {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      if (maxRight - maxLeft < right - left) {
        maxRight = right;
        maxLeft = left;
      }
      left--;
      right++;
    }
  };

  for (let i = 0; i < s.length; i++) {
    expandWindow(i, i); // odd length palindrome
    expandWindow(i, i + 1); // even length palindrome
  }

  return s.slice(maxLeft, maxRight + 1);
}
