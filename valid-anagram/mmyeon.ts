/**
 *
 * 접근 방법 :
 *  - 두 문자 정렬하면 O(nlogn)이니까 정렬 대신 객체 사용해서 빈도수 체크하는 방법으로 선택
 *  - 첫 번쨰 문자열 순회해서 객체에 문자별 빈도수 저장하고, 두 번째 문자열 순회하면서 빈도수 감소시키기
 *  - 모든 문자의 빈도수가 0이 되어야 anagram이라는 의미니까, 0인 경우 true 리턴
 *
 * 시간복잡도 :
 *  - 두 객체 for문으로 순회해야 하니까 O(n)
 *
 * 공간복잡도 :
 *  - 문자 빈도수를 객체의 크기는 입력 문자열 길이에 비레하니까 O(n)
 *
 */

function isAnagram(s: string, t: string): boolean {
  // 두 문자열 길이가 다른 경우는 anagram이 될 수 없으니까 초기 리턴 처리
  if (s.length !== t.length) return false;

  const charCount: Record<string, number> = {};

  for (const letter of s) {
    charCount[letter] = (charCount[letter] ?? 0) + 1;
  }

  for (const letter of t) {
    if (!charCount[letter]) return false;
    charCount[letter]--;
  }

  for (const count in charCount) {
    if (charCount[count] !== 0) return false;
  }

  return true;
}
