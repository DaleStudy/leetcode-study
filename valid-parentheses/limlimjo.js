/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  // 괄호 관리 스택
  const stack = [];

  // 여는 괄호, 닫는 괄호 매핑
  const brackets = { "(": ")", "{": "}", "[": "]" };

  // for문 돌며 확인
  for (let i of s) {
    // 여는 괄호일 경우
    if (brackets[i]) {
      stack.push(brackets[i]);
      // 닫는 괄호일 경우
    } else if (i !== stack.pop()) {
      return false;
    }
  }
  return true;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
