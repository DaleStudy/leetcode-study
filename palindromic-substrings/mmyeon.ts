/**
 *
 * 접근 방법 :
 * - 각 문자열에서 회문 조건 충족하는 경우 중심을 기준으로 확장해나가기 위해 투 포인터 사용
 * - 문자가 같고 범위 내에 있는 경우 확장해나가면서 횟수 업데이트
 * - 홀수 회문과 다르게 짝수 회문은 중심을 2문자에서 시작되어야 하니까 인덱스 별도 처리
 *
 * 시간복잡도 : O(n^2)
 * - 문자열 길이가 n일 때, for문에서 각 문자마다 최대 문자열 길이까지 비교하니까 O(n^2)
 *
 * 공간복잡도 : O(1)
 *
 */

function countPalindromes(s: string, left: number, right: number): number {
  let count = 0;

  while (0 <= left && right < s.length && s[left] === s[right]) {
    count++;
    left--;
    right++;
  }

  return count;
}

function countSubstrings(s: string): number {
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    // 홀수 회문 카운트
    count += countPalindromes(s, i, i);
    // 짝수 회문 카운트
    count += countPalindromes(s, i, i + 1);
  }
  return count;
}
