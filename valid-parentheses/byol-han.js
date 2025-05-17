function isValid(s) {
  const stack = [];
  const bracketMap = {
    ")": "(",
    "}": "{",
    "]": "[",
  };

  for (let char of s) {
    if (char === "(" || char === "{" || char === "[") {
      stack.push(char);
    } else {
      // 닫는 괄호가 나왔을 때 스택이 비었거나 짝이 안 맞는 경우
      if (stack.pop() !== bracketMap[char]) {
        return false;
      }
    }
  }

  // 모든 괄호가 짝지어졌는지 확인
  return stack.length === 0;
}
