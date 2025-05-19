/**
 * 괄호 문자열 유효성 검사
 *
 * 스택 자료구조 활용
 * 1. 괄호 쌍을 매핑하는 객체를 생성하고 조건을 확인
 * 2. 열린 괄호를 만나면 해당하는 닫힌 괄호를 스택에 직접 push
 * 3. 닫는 괄호를 만났을 때, 스택이 비어있거나 짝이 맞지 않으면 false
 * 4. 문자열을 모두 처리한 후, 스택이 비어있어야(문자열 길이가 0이어야) 모든 괄호가 올바르게 짝지어진 것(true)
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  // 빈 문자열이나 홀수 길이는 유효하지 않음
  if (s.length === 0 || s.length % 2 !== 0) return false;

  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    if (char === '(') {
      stack.push(')');
    } else if (char === '{') {
      stack.push('}');
    } else if (char === '[') {
      stack.push(']');
    } else if (stack.length === 0 || stack.pop() !== char) {
      // 닫는 괄호를 만났을 때, 스택이 비어있거나 짝이 맞지 않음
      return false;
    }
  }

  return stack.length === 0;
};
