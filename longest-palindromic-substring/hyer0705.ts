// Time Complexity: O(n^2), n: s의 길이
// Space Complexity: O(1)
function longestPalindrome(s: string): string {
  const expandAroundCenter = (s: string, left: number, right: number): [number, number] => {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left--;
      right++;
    }

    return [left + 1, right - 1];
  };

  let longest = "";
  for (let i = 0; i < s.length; i++) {
    const [s1, e1] = expandAroundCenter(s, i, i);
    const [s2, e2] = expandAroundCenter(s, i, i + 1);

    const odd = e1 - s1 + 1;
    const even = e2 - s2 + 1;

    if (longest.length < odd) {
      longest = s.slice(s1, e1 + 1);
    }

    if (longest.length < even) {
      longest = s.slice(s2, e2 + 1);
    }
  }

  return longest;
}
