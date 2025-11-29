var numDecodings = function (s) {
  const N = s.length;
  const memo = {};

  function dfs(i) {
    if (i === N) return 1;
    if (s[i] === "0") return 0; // 0은 단독으로 decode 불가능
    if (memo[i] !== undefined) return memo[i];

    // 1자리
    let count = dfs(i + 1);

    // 2자리
    if (i + 1 < N && Number(s.slice(i, i + 2)) <= 26) {
      count += dfs(i + 2);
    }

    memo[i] = count;
    return count;
  }

  return dfs(0);
};
