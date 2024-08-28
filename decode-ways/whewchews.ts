function numDecodings(s: string): number {
  // SC: O(N)
  const memo: { [key: number]: number } = { [s.length]: 1 };

  // TC: O(N)
  const dfs = (start: number): number => {
    if (start in memo) {
      return memo[start];
    }

    if (s[start] === "0") {
      // 0으로 시작하는 경우 가능한 경우의 수가 없음
      memo[start] = 0;
    } else if (
      start + 1 < s.length &&
      parseInt(s.substring(start, start + 2)) < 27
    ) {
      // 다음에 오는 글자가 두글자 이상 있고, start start+1 두글자가 1~26 사이의 값인 경우
      memo[start] = dfs(start + 1) + dfs(start + 2);
    } else {
      // 1글자만 남은 경우 or 첫 두글자가 27보다 큰 경우
      memo[start] = dfs(start + 1);
    }

    return memo[start];
  };

  // SC: 재귀호출 O(N)
  return dfs(0);
}

// TC: O(N)
// SC: O(N)
