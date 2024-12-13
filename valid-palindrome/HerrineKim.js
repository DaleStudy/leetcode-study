// 시간복잡도: O(n)

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  // 전처리 - 알파벳과 숫자만 남기고 소문자로 변환
  const cleanString = s.toLowerCase().replace(/[^a-z0-9]/g, "");

  // 양 끝에서 포인터를 이동하며 확인
  let left = 0, right = cleanString.length - 1;

  while (left < right) {
    if (cleanString[left] !== cleanString[right]) {
      return false; // 대칭이 깨지면 false
    }
    left++;
    right--;
  }

  return true; // 대칭이 유지되면 true
};
