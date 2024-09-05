/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  // 1. 아래 방식은 O(n^2)에 수렴함
  // s의 구성요소들을 소문자로 변환 후 배열에 넣고
  // 현재 길이가 2 이상이라면
  // shift === pop 이면 true 아니면 false

  // 2. 투 포인터 사용

  let str = s.toLowerCase().replace(/[^a-z0-9]/g, "");

  // 두 포인터 사용: 시작과 끝에서부터 비교
  let left = 0;
  let right = str.length - 1;

  while (left < right) {
    if (str[left] !== str[right]) {
      return false; // 두 문자가 다르면 palindrome 아님
    }

    left++;
    right--;
  }

  return true;
};
