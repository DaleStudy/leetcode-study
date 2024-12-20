// 시간복잡도: O(n)
// 공간복잡도: O(n)

/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  const memo = {};

  const helper = (index) => {
    if (index === s.length) return 1;
    if (s[index] === '0') return 0;
    if (memo[index] !== undefined) return memo[index];

    let ways = helper(index + 1);
    if (index < s.length - 1 && parseInt(s.slice(index, index + 2)) <= 26) {
      ways += helper(index + 2);
    }

    memo[index] = ways;
    return ways;
  };

  return helper(0);
};
