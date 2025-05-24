/**
 * 문제 설명
 * - 주어진 문자열 s의 모든 부분 문자열 중 팰린드롬인 문자열의 개수를 반환
 *
 * 아이디어
 * 1) 1. Brute Force O(n^3)
 * 2) 투포인터 O(n^2)
 *   - 짝수, 홀수 두 가지 경우로 나누어 탐색
 *   - 순회하면서 각 항목을 중심으로 좌우로 확장하며 팰린드롬인지 확인
 * 3) DP O(n^2)
 *   - dp[i][j]를 만들어서 s[i..j]가 팰린드롬인지 저장 -> 다음번에 해보기
 */
function countSubstrings(s: string): number {
  let result = 0;

  for (let i = 0; i < s.length; i++) {
    let left = i;
    let right = i;

    while (left >= 0 && right < s.length && s[left] === s[right]) {
      result++;
      left--;
      right++;
    }

    left = i;
    right = i + 1;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      result++;
      left--;
      right++;
    }
  }
  return result;
}
