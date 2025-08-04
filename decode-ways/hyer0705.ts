function numDecodings(s: string): number {
  const sLen = s.length;
  const isValid = (s: string): boolean => {
    if (s[0] === "0") return false;

    return Number(s) > 0 && Number(s) <= 26;
  };

  if (sLen === 0) return 0;
  if (s.length === 1) return isValid(s[0]) ? 1 : 0;

  // dp[i]: i번째 위치까지 디코딩할 수 있는 방법의 수
  const dp: number[] = Array(sLen).fill(0);
  dp[0] = isValid(s[0]) ? 1 : 0;
  dp[1] = (isValid(s[1]) ? dp[0] : 0) + (isValid(s.substring(0, 2)) ? 1 : 0);

  for (let i = 2; i < sLen; i++) {
    const singleDigitWays = isValid(s[i]) ? dp[i - 1] : 0;
    const doubleDigitWays = isValid(s[i - 1] + s[i]) ? dp[i - 2] : 0;

    dp[i] = singleDigitWays + doubleDigitWays;
  }

  return dp[sLen - 1];
}
