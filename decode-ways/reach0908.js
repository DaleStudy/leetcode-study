/**
 * 시간복잡도: O(n)
 * 실행속도: 65ms
 * @param {string} s
 * @return {number}
 */
const numDecodings = function (s) {
  const n = s.length;

  const memo = new Array(n + 1).fill(0);

  function dfs(i) {
    if (i === n) {
      return 1;
    }

    if (s[i] === "0") {
      return 0;
    }

    if (memo[i]) {
      return memo[i];
    }

    let res = dfs(i + 1);

    if (i + 1 < n && Number(s.slice(i, i + 2) <= 26)) {
      res += dfs(i + 2);
    }

    memo[i] = res;

    return res;
  }

  return dfs[0];
};

/**
 * 시간복잡도: O(n)
 * 실행속도: 0~1ms
 * @param {string} s
 * @return {number}
 */
/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
var numDecodings2 = function (s) {
  const memo = new Map();
  memo.set(s.length, 1);

  function dfs(start) {
    if (memo.has(start)) {
      return memo.get(start);
    }

    if (s[start] === "0") {
      memo.set(start, 0);
    } else if (
      start + 1 < s.length &&
      parseInt(s.slice(start, start + 2)) < 27
    ) {
      memo.set(start, dfs(start + 1) + dfs(start + 2));
    } else {
      memo.set(start, dfs(start + 1));
    }

    return memo.get(start);
  }

  return dfs(0);
};
