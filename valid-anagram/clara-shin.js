/**
 * 두 문자열 s와 t가 서로 애너그램(anagram)인지 확인하는 문제
 * 애너그램: 글자의 배열 순서는 다르지만 구성하는 문자와 각 문자의 개수가 동일한 문자열
 *
 * 접근 방법 몇 가지:
 * 1. 정렬 방식: 두 문자열을 알파벳 순으로 정렬한 후 비교하는 방법
 * 2-1. 문자 카운팅 방식 (객체활용): 각 문자열에 등장하는 문자들의 빈도수를 계산하여 비교하는 방법
 * 2-2. 문자 카운팅 방식 (해시맵 객체활용): 문자를 키로, 빈도수를 값으로 하는 해시맵을 만들어 비교하는 방법
 *
 * 팔로우업 질문: 입력에 유니 코드 문자가 포함되어 있으면 어떻게 해? 그러한 경우에 솔루션을 어떻게 조정할꺼야?
 * JavaScript의 문자열은 기본적으로 UTF-16으로 인코딩되서 유니코드 문자도 처리 가능
 * Map 객체는 어떤 타입의 키도 허용 ➡️ 유니코드 문자를 키로 사용하는 데 문제가 없음
 * (방법 2-1)의 일반 객체도 유니코드 문자를 키로 지원하지만, Map을 사용하는 것이 좀 더 안전 => 해시맵으로 구현 ㄱㄱ
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
function isAnagram(s, t) {
  // 길이가 다르면 애너그램이 될 수 없음 (빠른 리턴)
  if (s.length !== t.length) {
    return false;
  }

  const charMap = new Map();

  // 첫 번째 문자열의 각 문자 카운트 증가
  for (let char of s) {
    charMap.set(char, (charMap.get(char) || 0) + 1);
  }

  // 두 번째 문자열의 각 문자 카운트 감소
  for (let char of t) {
    const count = charMap.get(char);

    // 해당 문자가 없거나 카운트가 0이면 애너그램이 아님
    if (!count) {
      return false;
    }

    charMap.set(char, count - 1);
  }

  // 모든 카운트가 0인지 확인
  for (let count of charMap.values()) {
    if (count !== 0) {
      return false;
    }
  }

  return true;
}
