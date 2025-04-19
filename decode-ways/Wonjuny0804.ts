function numDecodings(s: string): number {
  const memo: Record<number, number> = {};

  const dfs = (index: number): number => {
      if (index === s.length) return 1;
      if (s[index] === '0') return 0;

      if (memo[index] !== undefined) return memo[index];

      let res = dfs(index + 1);

      if (index + 1 < s.length && Number(s.slice(index, index + 2)) <= 26) {
          res += dfs(index + 2);
      }

      memo[index] = res;
      return res;
  }

  return dfs(0);
}