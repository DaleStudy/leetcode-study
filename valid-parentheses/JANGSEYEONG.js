/**
 * 시간복잡도: O(n) - 문자열의 각 문자를 한 번씩만 순회
 * 공간복잡도: O(n) - 최악의 경우 모든 문자가 여는 괄호일 때 스택에 n개 저장
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const length = s.length;
  if (length % 2 === 1) return false; // 홀수일 경우 바로 return false

  const MATCHES = { "(": ")", "{": "}", "[": "]" };

  // 여는 괄호가 나오면 스택에 저장, 닫는 괄호가 나오면 스택의 마지막 여는 괄호와 비교
  const stack = [];
  for (let char of s) {
    if (char in MATCHES) {
      stack.push(char);
    } else if (MATCHES[stack.pop()] !== char) {
      return false;
    }
  }
  // 짝이 맞으면 size 0
  return stack.length === 0;
};
