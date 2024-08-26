/**
 * @description
 * brainstorming:
 * 1. dp -> dp[i] = dp[i-1] + count
 * 2. recursive function
 *
 * strategy:
 * https://www.algodale.com/problems/decode-ways/
 *
 * result:
 * 1. couldn't think of the conditions
 *      true: 1~9, 10~27
 *      false: 0, 0N, 28↑
 * 2. persist solution that is top down
 */

// https://www.algodale.com/problems/decode-ways/ Solve 1
/**
 * time complexity: O(2^n)
 * space complexity: O(n)
 */
var numDecodings = function (s) {
  const search = (start) => {
    if (start === s.length) return 1;
    if (s[start] === "0") return 0;
    if (start + 1 < s.length && Number(`${s[start]}${s[start + 1]}`) < 27) {
      return search(start + 1) + search(start + 2);
    }
    return search(start + 1);
  };

  return search(0);
};

// https://www.algodale.com/problems/decode-ways/ Solve 2
/**
 * time complexity: O(2^n)
 * space complexity: O(n)
 */
var numDecodings = function (s) {
  const memo = new Map();
  memo.set(s.length, 1);

  const search = (start) => {
    if (!!memo.get(start)) return memo.get(start);

    if (s[start] === "0") memo.set(start, 0);
    else if (start + 1 < s.length && Number(`${s[start]}${s[start + 1]}`) < 27)
      memo.set(start, search(start + 1) + search(start + 2));
    else memo.set(start, search(start + 1));

    return memo.get(start);
  };

  return search(0);
};

// https://www.algodale.com/problems/decode-ways/ Solve 3
/**
 * time complexity: O(n)
 * space complexity: O(n)
 */
var numDecodings = function (s) {
  const dp = Array.from({ length: s.length + 1 }, (_, i) =>
    i === s.length ? 1 : 0
  );

  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] === "0") dp[i] = 0;
    else if (i + 1 < s.length && Number(`${s[i]}${s[i + 1]}`) < 27)
      dp[i] = dp[i + 1] + dp[i + 2];
    else dp[i] = dp[i + 1];
  }

  return dp[0];
};
