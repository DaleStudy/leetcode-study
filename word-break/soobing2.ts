/**
 * 유형
 * - dp (뒤쪽 단어를 쪼갤 수 있어야 전체를 쪼갤 수 있다.)
 *
 * 문제 설명
 * - 문자열 s를 주어진 wordDict에 있는 단어로 쪼갤 수 있는가?
 *
 * 아이디어
 * - dp[i] = s[i]로 시작하는 문자열이 wordDict에 있는 단어로 쪼갤 수 있는지 여부
 */

function wordBreak(s: string, wordDict: string[]): boolean {
  const dp = new Array(s.length + 1).fill(false);

  dp[s.length] = true;

  for (let i = s.length - 1; i >= 0; i--) {
    for (const word of wordDict) {
      if (i + word.length <= s.length && s.slice(i, i + word.length) === word) {
        dp[i] = dp[i + word.length];
      }
      if (dp[i]) break;
    }
  }
  return dp[0];
}
