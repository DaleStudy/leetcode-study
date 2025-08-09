/**
 * 문제 유형
 * - 문자열 처리, 문자열 비교
 *
 * 문제 설명
 * - 주어진 문자열이 팰린드롬인지 확인하는 문제
 *
 * 아이디어
 * 1) 주어진 문자열에서 숫자, 알파벳만 남겨두고 소문자로 변환 후에 팰린드롬인지 확인
 */
function isPalindrome(s: string): boolean {
  const original = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
  const reverse = original.split("").reverse().join("");
  return original === reverse;
}
