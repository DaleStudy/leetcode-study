/**
 * 핵심 아이디어:
 * 1. 정규표현식으로 알파벳과 숫자만 추출하여 소문자로 변환
 * 2. Two Pointer 방식으로 양 끝에서 중앙으로 이동하며 비교
 *
 * @param {string} s - 검사할 문자열
 * @return {boolean} - 팰린드롬 여부
 *
 * 시간 복잡도: O(n)
 * - replace() 메서드: O(n) - 문자열 전체 순회
 * - toLowerCase(): O(n) - cleaned 문자열 순회
 * - while 루프: O(n/2) → O(n) - 최대 문자열 길이의 절반만큼 반복
 * - 전체: O(n) + O(n) + O(n) = O(n)
 *
 * 공간 복잡도: O(n)
 * - cleaned 문자열: O(n) - 최악의 경우 입력 문자열의 모든 문자가 알파벳/숫자
 * - left, right 포인터 변수: O(1)
 * - 전체: O(n)
 */
const isPalindrome = (s) => {
  // 알파벳과 숫자만 남기고 소문자로 변환
  // \W는 알파벳, 숫자, 언더스코어를 제외한 모든 문자
  // _도 제거해야 하므로 [^a-zA-Z0-9] 사용
  const cleaned = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

  // Two Pointer 접근법
  let left = 0;
  let right = cleaned.length - 1;

  // 양 끝에서 중앙으로 이동하며 비교
  while (left < right) {
    if (cleaned[left] !== cleaned[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
};
