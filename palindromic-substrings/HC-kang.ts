/*
647. Palindromic Substrings

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 */

// Time complexity: O(n^3)
// Space complexity: O(n^3)
function countSubstrings(s: string): number {
  function isPalindrome(s: string): boolean {
    if (s.length === 0) return false;
    if (s.length === 1) return true;
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
      if (s[left] !== s[right]) return false;
      left++;
      right--;
    }
    return true;
  }

  const candidates = new Map<string, number>();
  for (let i = 0; i < s.length; i++) {
    for (let j = i + 1; j <= s.length; j++) {
      // this will cost both t.c. and s.c. O(n^3)
      candidates.set(s.slice(i, j), (candidates.get(s.slice(i, j)) || 0) + 1);
    }
  }

  let count = 0;
  for (const [key, value] of candidates) {
    if (isPalindrome(key)) count += value
  }

  return count;
};

// Time complexity: O(n^3)
// Space complexity: O(1)
function countSubstrings(s: string): number {
  function isPalindrome(s: string): boolean {
    if (s.length === 0) return false;
    if (s.length === 1) return true;
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
      if (s[left] !== s[right]) return false;
      left++;
      right--;
    }
    return true;
  }

  let count = 0;
  for (let i = 0; i < s.length; i++) {
    for (let j = i + 1; j <= s.length; j++) {
      // this will cause t.c. O(n^3). need to optimize this part
      if (isPalindrome(s.slice(i, j))) count++;
    }
  }

  return count;
}

// Time complexity: O(n^2)
// Space complexity: O(1)
function countSubstrings(s: string): number {
  function expandIsPalindrome(left: number, right: number): number {
    let count = 0;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      count++;
      left--;
      right++;
    }
    return count;
  }

  let count = 0;
  for (let i = 0; i < s.length; i++) {
    count += expandIsPalindrome(i, i);
    count += expandIsPalindrome(i, i + 1);
  }
  return count;
}
