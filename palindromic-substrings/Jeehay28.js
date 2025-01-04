/**
 * @param {string} s
 * @return {number}
 */

// TC : O(n^2)
// SC : O(1)

var countSubstrings = function (s) {
  // For each character in the string, treat it as the center of a potential palindrome.

  // 'Count Palindromic Substrings' helper function
  const countPS = (left, right) => {
    let cnt = 0;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      cnt += 1;
      left -= 1;
      right += 1;
    }
    return cnt;
  };

  let totCnt = 0;

  for (let i = 0; i < s.length; i++) {
    // left === right : 1 center point, odd-length palindromic
    totCnt += countPS(i, i);

    // left !== right : 2 center points, even-length palindromic
    totCnt += countPS(i, i + 1);
  }

  return totCnt;
};



