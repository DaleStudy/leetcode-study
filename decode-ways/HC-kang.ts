// T.C: O(n)
// S.C: O(n)
function numDecodings(s: string): number {
  const NUM_OF_ALPHA = 26;
  const memo = new Map<number, number>();

  function dfs(idx: number): number {
    if (idx === s.length) {
      return 1;
    }
    if (s[idx] === '0') {
      return 0;
    }
    if (memo.has(idx)) {
      return memo.get(idx)!;
    }

    let count = dfs(idx + 1);
    if (
      idx + 2 <= s.length && // check if idx + 2 is in the range
      parseInt(s.slice(idx, idx + 2), 10) <= NUM_OF_ALPHA
    ) {
      count += dfs(idx + 2);
    }

    memo.set(idx, count);
    return count;
  }

  return dfs(0);
}
