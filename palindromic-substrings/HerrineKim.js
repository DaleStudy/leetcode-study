// 시간 복잡도: O(n^2)
// 공간 복잡도: O(1)

/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
  let count = 0;

  const countPalindrome = (left, right) => {
      while (left >= 0 && right < s.length && s[left] === s[right]) {
          count++;
          left--;
          right++;
      }
  };

  for (let i = 0; i < s.length; i++) {
      countPalindrome(i, i);
      countPalindrome(i, i + 1);
  }

  return count;
};
