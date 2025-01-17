// "leetcode"
// [ true, false, false, false, true, false, false, false, true ]
/**
 * 접근 방법 : DP 바텀업 방식
 * - 문자열 늘려가면서, 부분 문자열에 wordDict에 포함되는지 체크
 *
 * 시간복잡도 : O(n^2)
 *  - n은 문자열 s의 길이
 *  - 외부 반복문에서 문자열 순회(n번), 내부 반복문에서 최대 n번 순회
 *
 * 공간복잡도 : O(n)
 *  - 문자열 길이 n만큼 dp 배열 저장
 */
function wordBreak(s: string, wordDict: string[]): boolean {
  const set = new Set(wordDict);
  const dp = Array(s.length + 1).fill(false);
  // 빈 문자열은 항상 나눌 수 있으니까 true
  dp[0] = true;

  // i는 문자열의 끝 인덱스
  for (let i = 1; i <= s.length; i++) {
    // j는 문자열의 시작 인덱스
    for (let j = 0; j < i; j++) {
      if (dp[j] && set.has(s.substring(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[s.length];
}
