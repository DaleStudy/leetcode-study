/**
 * 정규표현식으로 알파벳과 숫자만 남기고 소문자로 변환 후, 양 끝에서부터 비교
 * 시간복잡도 O(n)
 * 공간복잡도 O(n)
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let newArr = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
  let answer = true;
  for (let i = 0; i < Math.ceil(newArr.length / 2); i++) {
    if (newArr[i] !== newArr[newArr.length - 1 - i]) {
      answer = false;
      return answer;
    }
  }
  return answer;
};
