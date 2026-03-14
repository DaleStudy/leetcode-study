/**
 * @description 문자의 종류와 개수가 완전히 같은 애너그램인지 판별
 * @param {string} s 문자열 1
 * @param {string} t 문자열 2
 * @returns {boolean} 애너그램 여부
 */
function isAnagram(s: string, t: string): boolean {
  // 문자열들의 길이가 다르면 애너그램 아님
  if (s.length !== t.length) return false;

  // 영어 소문자 개수 "a"~"z" = 26개
  const LOWER_ALPHABET_COUNT = 26;
  // 알파벳 등장 횟수를 저장할 배열
  // index 0 -> 'a'
  // index 1 -> 'b'
  const count = new Array(LOWER_ALPHABET_COUNT).fill(0);
  // a의 아스키코드
  const BASE = "a".charCodeAt(0);

  for (let i = 0; i < s.length; i++) {
    count[s.charCodeAt(i) - BASE]++;
    count[t.charCodeAt(i) - BASE]--;
  }

  // 모든 문자의 등장 횟수가 0이면
  // s와 t의 문자 종류와 개수가 완전히 동일
  return count.every((value) => value === 0);
}
