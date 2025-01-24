// 시간복잡도: O(n)
// 공간복잡도: O(n)

// 스택을 사용하여 괄호의 유효성을 검사
// 괄호가 열리면 스택에 추가하고 닫히면 스택에서 마지막 요소를 꺼내서 짝이 맞는지 확인
// 스택이 비어있으면 유효한 괄호 문자열

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const bracketStack = [];
  const bracketPairs = {
    ')': '(',
    '}': '{',
    ']': '['
  };

  for (const char of s) {
    if (char in bracketPairs) {
      const lastChar = bracketStack.pop();

      if (lastChar !== bracketPairs[char]) {
        return false;
      }
    } else {
      bracketStack.push(char);
    }
  }

  return bracketStack.length === 0;
};
