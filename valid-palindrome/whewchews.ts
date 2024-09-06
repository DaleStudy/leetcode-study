/*
 * 조건
 * 모든 대문자를 소문자로 바꿔서 처리
 * 영어 대소문자, 숫자가 아닌 문자는 제거 후 체크
 *
 * 아이디어
 * 정규식으로 문자열 중에 숫자, 문자만 추출
 * 짝수인 경우 123456
 * 1-6, 2-5, 3-4를 비교: length/2번 비교
 * 홀수인 경우 1234567
 * 1-7, 2-6, 3-5를 비교: length/2번 비교
 */

function isPalindrome(s: string): boolean {
  // TC: O(n)
  // SC: O(n)
  const str = s
    .replace(/[^a-zA-Z0-9]/g, "")
    .replace(/\s+/g, "")
    .toLocaleLowerCase();
  const len = str.length;

  // TC: O(n)
  for (let i = 0; i <= str.length / 2 - 1; i++) {
    if (str[i] !== str[len - i - 1]) {
      return false;
    }
  }

  return true;
}

// TC: O(n)
// SC: O(n)
