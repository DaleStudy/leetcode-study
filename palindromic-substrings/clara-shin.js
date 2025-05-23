/**
 * 주어진 문자열에서 팰린드롬(앞뒤로 읽어도 같은 문자열)인 부분 문자열의 개수를 구하는 문제
 *
 * 투 포인터(Two Pointers) vs. 중심확장(Center Expansion)
 * 투포인터: 보통 정렬된 배열에서 두 요소의 합을 찾는 등에 사용
 *
 * 중심확장이 더 적합한 이유:
 * 팰린드롬의 특성(중심 대칭)을 직접적으로 활용
 * 불필요한 비교 최소화
 * 구현이 간단하고 이해하기 쉬움
 *
 * 이번 문제는: Center Expansion 방법으로 접근
 * 모든 부분 문자열을 확인해야 함
 * 각 위치에서 팰린드롬 가능성을 체크해야 함
 *
 * 시간 복잡도: O(n²) - 각 중심에서 최대 n번 확장
 * 공간 복잡도: O(1) - 추가 공간 거의 불필요
 */
/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
  if (!s || s.length === 0) return 0; // 빈 배열이면 빠른 리턴

  let count = 0;
  const n = s.length;

  // 중심 확장 함수
  function expandAroundCenter(left, right) {
    while (left >= 0 && right < n && s[left] === s[right]) {
      count++;
      left--;
      right++;
    }
  }

  for (let i = 0; i < n; i++) {
    // 홀수 길이 팰린드롬
    expandAroundCenter(i, i);
    // 짝수 길이 팰린드롬
    expandAroundCenter(i, i + 1);
  }

  return count;
};
