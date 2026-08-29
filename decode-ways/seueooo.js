/**
0부터 i번 인덱스 문자열 내에서 해석가능한 조합 개수를 dp에 저장
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  if (s[0] === "0") return 0;
  let dp = new Array(s.length).fill(0);
  dp[0] = 1;
  for (let i = 1; i < s.length; i++) {
    if (s[i] !== "0") {
      dp[i] += dp[i - 1];
    }

    // 두 자리 수인 경우 (마지막 두덩이를 하나로 생각)
    const two = Number(s.slice(i - 1, i + 1));

    if (two >= 10 && two <= 26) {
      if (i === 1) {
        dp[i] += 1;
      } else dp[i] += dp[i - 2];
    }
  }
  return dp[s.length - 1];
};
