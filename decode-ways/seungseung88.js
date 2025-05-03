/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
var numDecodings = function (s) {
  const memo = new Map();
  memo.set(s.length, 1);

  function dfs(start) {
    if (memo.has(start)) {
      return memo.get(start);
    }

    if (s[start] === '0') {
      memo.set(start, 0);
    } else if (start + 1 < s.length && parseInt(s.slice(start, start + 2)) < 27) {
      memo.set(start, dfs(start + 1) + dfs(start + 2));
    } else {
      memo.set(start, dfs(start + 1));
    }

    return memo.get(start);
  }

  return dfs(0);
};
