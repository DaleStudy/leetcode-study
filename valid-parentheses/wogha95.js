/**
 * TC: O(S)
 * s 매개변수의 길이만큼 순회 1번
 *
 * SC: O(S)
 * 최악의 경우 S의 길이만큼 stack 배열에 모두 push 할 수 있기 때문에
 *
 * S: s.length
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const map = {
    "(": ")",
    "{": "}",
    "[": "]",
  };
  const stack = [];

  // 1. s의 길이만큼 순회를 하면서
  for (const char of s) {
    // 2. 열린 괄호라면 stack에 짝지어진 닫힌 괄호를 저장
    // 3. 닫힌 괄호라면 stack에서 꺼낸 것과 동일한지 확인
    switch (char) {
      case "(":
      case "{":
      case "[":
        stack.push(map[char]);
        break;
      case "}":
      case ")":
      case "]":
        if (stack.pop() !== char) {
          return false;
        }
    }
  }

  // 4. 남은 괄호가 없는지 확인
  return stack.length === 0;
};
