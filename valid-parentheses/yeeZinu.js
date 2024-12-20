/**
 * @param {string} s
 * @return {boolean}

 괄호 유효성 검사(
 어느 괄호로 열어도 상관은 없지만 열었으면 닫아야지 true 안닫으면 false
 ({)} -> 이런식으로 중간에 섞여서 닫혀있지 않다는 전제의 문제
 */
var isValid = function (s) {
  if (s.length % 2 === 1) {
    return false
  }

  // 괄호들이 들어갈 스택배열
  const stack = [];

  // 괄호 짝 객체
  const pair = {
    "(": ")",
    "{": "}",
    "[": "]",
  }

  for (let i = 0; i < s.length; i++) {
    // 열린괄호면 스택추가
    if (s[i] in pair) {
      stack.push(s[i]);
    }
    // 닫힌 괄호라면?
    else {
      // 스택배열의 마지막이 같은 종류의 괄호라면 제거
      if (pair[stack.at(-1)] === s[i]) {
        stack.pop();
      }
      // 아니면 false
      else {
        return false
      }
    }
  }
  // 스택배열이 비었으면 true
  return stack.length === 0;
};
