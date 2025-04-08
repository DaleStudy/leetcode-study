/**
 * Source: https://leetcode.com/problems/valid-anagram/
 * 요점: 두 문자열이 애너그램인지 확인하는 함수
 * 풀이 시간: 5분
 * 풀이방법: 문자열을 정렬하여 비교하는 방법과 문자 빈도수를 카운팅하는 방법
 * 시간복잡도: O(n log n) - 정렬이 지배적인 연산
 * 공간복잡도: O(n) - 문자열을 배열로 변환하기 위한 공간
 */
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;
  return s.split("").sort().join() === t.split("").sort().join();
}

/**
 * Solution2: 자료구조 Map을 사용해서 문자 빈도를 계산해 두 문자열이 애너그램인지 확인하기
 * 시간복잡도: O(n) - 단일 순회로 해결
 * 공간복잡도: O(1) - 최대 26개 알파벳에 대한 고정 크기 맵 사용
 */
function isAnagram2(s: string, t: string): boolean {
  // 길이가 다르면 애너그램이 될 수 없음
  if (s.length !== t.length) return false;

  // 각 문자의 출현 빈도를 기록할 목적으로 Map을 사용
  const charCount = new Map<string, number>();

  // 첫 번째 문자열의 각 문자 빈도 증가
  for (const char of s) {
    charCount.set(char, (charCount.get(char) || 0) + 1);
  }

  // 두 번째 문자열의 각 문자 빈도 감소
  for (const char of t) {
    const count = charCount.get(char);

    // 문자가 없거나 빈도가 0이면 애너그램이 아님
    if (count === undefined || count === 0) return false;

    charCount.set(char, count - 1);
  }

  return true;
}
