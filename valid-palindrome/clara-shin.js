/**
 * 문자열이 팰린드롬인지 확인하는 함수
 * 팰린드롬 판단:
 * 대문자를 소문자로 변환
 * 영숫자(알파벳이랑 숫자)만 남기고 나머지 제거 => 정규식 알면 편함
 * 앞에서 읽으나 뒤에서 읽으나 같아야 함
 */

/**정규식 없이 문자열 뒤집는 방법
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  s = s.toLowerCase();

  let str = ''; // 영숫자만 남길 문자열
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    // 알파벳이거나 숫자면 str에 추가
    if ((char >= 'a' && char <= 'z') || (char >= '0' && char <= '9')) {
      str += char;
    }
  }

  // 문자열 뒤집기
  let reversedStr = str.split('').reverse().join('');

  return str === reversedStr;
};

/**정규식 사용한 투 포인터 방법
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome2 = function (s) {
  const str = s.toLowerCase().replace(/[^a-z0-9]/g, ''); // 영숫자만 남기

  // 투 포인터
  let left = 0;
  let right = str.length - 1;

  while (left < right) {
    if (str[left] !== str[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
};
