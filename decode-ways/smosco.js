/**
 * Decode Ways
 *
 * 핵심 아이디어:
 * - 숫자 문자열을 1-26(A-Z)로 디코딩하는 경우의 수를 구하는 문제
 * - DP[i] = i번째 위치까지의 디코딩 방법 수
 * - 각 위치에서 2가지 선택 가능:
 *   1) 한 자리 숫자로 해석 (1-9)
 *   2) 두 자리 숫자로 해석 (10-26)
 *
 * 시간 복잡도: O(n) - 문자열을 한 번만 순회
 * 공간 복잡도: O(n) - dp 배열 사용
 */

function numDecodings(s) {
  // 예외 처리: 빈 문자열이거나 '0'으로 시작하면 불가능
  if (!s || s[0] === '0') return 0;

  const n = s.length;
  const dp = new Array(n + 1).fill(0);

  // 초기값 설정
  dp[0] = 1; // 빈 문자열 (base case)
  dp[1] = 1; // 첫 번째 문자 (이미 '0' 체크 완료)

  // i번째 위치까지의 디코딩 방법 수 계산
  for (let i = 2; i <= n; i++) {
    // 1) 한 자리 숫자로 해석 (1~9만 가능, 0은 단독 불가)
    const oneDigit = s[i - 1];
    if (oneDigit !== '0') {
      dp[i] += dp[i - 1]; // 이전까지의 모든 방법에 현재 숫자 추가
    }

    // 2) 두 자리 숫자로 해석 (10~26만 가능)
    const twoDigits = s[i - 2] + s[i - 1];
    const twoDigitsNum = parseInt(twoDigits);
    if (twoDigitsNum >= 10 && twoDigitsNum <= 26) {
      dp[i] += dp[i - 2]; // i-2까지의 모든 방법에 두 자리 숫자 추가
    }
  }

  return dp[n];
}
