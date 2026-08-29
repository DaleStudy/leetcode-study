/**
s를 정규식으로 알파벳 소문자 string만 남겨둬야한다.
알파벳 소문자만 남겨놓도록 하는 정규식은 '/[^a-z0-9]/gi'이다.
left(0)와 right(마지막 인덱스)를 동시에 하나씩 줄여가면서 비교
 */

/**
 * @param {string} s
 * @return {boolean}
 */
function isPalindrome(s) {
  s = s.replace(/[^a-z0-9]/gi, "").toLowerCase();

  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (s[left] !== s[right]) {
      return false;
    }

    left++;
    right--;
  }

  return true;
}
