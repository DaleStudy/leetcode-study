/**
 * @param {string} s
 * @return {boolean}
 */
// TC: O(n) / SC: O(n)
var isPalindrome = function (s) {
  const processed = s.toLowerCase().replaceAll(/[^a-z0-9]+/g, '');
  const reversed = [...processed].reverse().join('');
  return processed === reversed;
};

// TC: O(n) / SC: O(1)
// With two pointers
var isPalindrome = function (s) {
  const nonAlphanumeric = /[^a-zA-Z0-9]+/;
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    while (left < right && nonAlphanumeric.test(s[left])) left++; // 단일 문자 테스트 O(1) 상수 취급
    while (left < right && nonAlphanumeric.test(s[right])) right--;
    if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;
    left++;
    right--;
  }

  return true;
};
