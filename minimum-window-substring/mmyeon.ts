/**
 * @link https://leetcode.com/problems/minimum-window-substring/description/
 * 접근 방법 : 2개의 포인터 활용해서 슬라이딩 윈도우 방식 사용
 * - t의 문자를 맵에 저장해서 개수 기록
 * - right 포인터로 t의 모든 문자 포함할 때까지 윈도우 확장
 * - 모든 문자 포함하면, left 포인터로 최소 윈도우 찾을 때까지 윈도우 축소
 * - '확장 => 축소 => 최소 윈도우 업데이트' 이 과정을 반복
 *
 * 시간복잡도 : O(n)
 *  - n은 s의 길이, 각 문자 최대 2회 방문 (확장 + 축소)
 *
 * 공간복잡도 : O(n)
 *  - 최악의 경우, 윈도우에 s의 모든 문자가 저장됨
 */
function minWindow(s: string, t: string): string {
  const targetCharCount = new Map<string, number>();

  // t의 문자 개수 카운트
  for (const char of t) {
    targetCharCount.set(char, (targetCharCount.get(char) ?? 0) + 1);
  }

  const requiredUniqueChars = targetCharCount.size;
  let matchedUniqueChars = 0;
  const windowCharCount = new Map<string, number>();

  let minWindow = "";
  let minWindowLength = Infinity;

  let left = 0,
    right = 0;

  while (right < s.length) {
    const char = s[right];
    windowCharCount.set(char, (windowCharCount.get(char) ?? 0) + 1);

    // t에 속하는 문자이면서, 문자 개수가 같은 경우
    if (
      targetCharCount.has(char) &&
      targetCharCount.get(char) === windowCharCount.get(char)
    )
      matchedUniqueChars++;

    while (matchedUniqueChars === requiredUniqueChars) {
      const windowLength = right - left + 1;

      // 최소 윈도우 업데이트
      if (windowLength < minWindowLength) {
        minWindowLength = windowLength;
        minWindow = s.substring(left, right + 1);
      }

      const leftChar = s[left];
      windowCharCount.set(leftChar, windowCharCount.get(leftChar)! - 1);

      //축소로 윈도우 내의 t문자가 감소했으면 matchedUniqueChars 감소
      if (windowCharCount.get(leftChar)! < targetCharCount.get(leftChar)!)
        matchedUniqueChars--;

      // 윈도우 축소
      left++;
    }

    // 윈도우 확장
    right++;
  }

  return minWindow;
}
