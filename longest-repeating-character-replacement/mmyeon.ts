/**
 * @link https://leetcode.com/problems/longest-repeating-character-replacement/
 *
 * 접근 방법 :
 *  - 문자열 순회하면서, 현재 윈도우 내 문자의 빈도수 저장
 *  - 윈도우 축소 조건 : 윈도우 크기 - 윈도우 내 최다 등장 문자의 개수 > k
 *      => k보다 다른 문자의 개수가 많은 경우, left 포인터 이동해서 윈도우 크기 줄이기
 *  - 윈도우 크기 조절하면서 최대 길이 업데이트
 *
 * 시간복잡도 : O(n)
 *  - 문자 n개만큼 1회 순회하면서 윈도우 크기 조절
 *
 * 공간복잡도 : O(1)
 *  - 대문자의 개수(26개)만큼 map에 저장
 */
function characterReplacement(s: string, k: number): number {
  const map = new Map<string, number>();
  let maxFrequency = 0,
    maxLength = 0,
    left = 0;

  for (let right = 0; right < s.length; right++) {
    const rightPositionChar = s[right];
    // 문자의 빈도수 map에 저장
    map.set(rightPositionChar, (map.get(rightPositionChar) ?? 0) + 1);
    maxFrequency = Math.max(maxFrequency, map.get(rightPositionChar)!);

    // 윈도우 축소해야 되는 경우 - k보다 다른 문자의 개수가 많은 경우
    if (right - left + 1 - maxFrequency > k) {
      map.set(s[left], map.get(s[left])! - 1);
      left++;
    }

    // 최대 길이 업데이트
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}
