/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
  let count = 0;

  const expand = (left, right) => {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      count++;
      left--;
      right++;
    }
  };

  for (let i = 0; i < s.length; i++) {
    expand(i, i); // 홀수 길이 중심 (예: "aba")
    expand(i, i + 1); // 짝수 길이 중심 (예: "aa")
  }

  return count;
};
