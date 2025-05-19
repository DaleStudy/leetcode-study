// [91] Decode Ways

/**
 * [Time Complexity]
 * O(n)
 *
 * [Space Complexity]
 * O(n)
 */
function numDecodings(s: string): number {
  const n = s.length;
  const memo = new Array<number>(n + 1).fill(0);

  // 첫번째 숫자가 0인 경우 디코딩이 불가능하므로 미리 0 반환
  if (s[0] === "0") return 0;

  memo[0] = 1; // 빈 문자열
  memo[1] = 1; // 0이 아닌 첫번째 숫자 디코딩

  for (let idx = 2; idx <= n; idx++) {
    const oneDigit = Number(s.slice(idx - 1, idx)); // 현재 숫자
    const twoDigits = Number(s.slice(idx - 2, idx)); // 현재 숫자 앞의 수와 합침

    // 변환할 수 있는 경우의 수를 더해준다.
    if (oneDigit >= 1 && oneDigit <= 9) {
      memo[idx] += memo[idx - 1];
    }
    if (twoDigits >= 10 && twoDigits <= 26) {
      memo[idx] += memo[idx - 2];
    }
  }

  return memo[n];
}
