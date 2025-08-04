/**
 * 문제 설명
 * - k번 문자 대체를 통해 가장 길게 반복되는 문자열 찾기
 *
 * 아이디어
 * 1) Sliding Window 활용
 *   - 투포인터 알고리즘을 활용하여 현재 윈도우 내에서 k번 문자 대체가 가능한지 체크하고,
 *     윈도우 크기를 조절하면서 최대 길이를 찾는다.
 *
 * 시간 복잡도
 * - O(n)
 *   - 문자열을 한번 순회하면서 윈도우 크기를 조절하기 때문에 O(n)의 시간 복잡도를 가진다.
 *
 * 공간 복잡도
 * - O(1)
 */

function characterReplacement(s: string, k: number): number {
  let start = 0;
  const map: Record<string, number> = {};
  let maxLength = 0;
  let maxCount = 0;
  for (let end = 0; end < s.length; end++) {
    map[s[end]] = (map[s[end]] || 0) + 1;
    maxCount = Math.max(maxCount, map[s[end]]);
    while (end - start + 1 - maxCount > k) {
      map[s[start]]--;
      start++;
    }

    maxLength = Math.max(end - start + 1, maxLength);
  }
  return maxLength;
}
