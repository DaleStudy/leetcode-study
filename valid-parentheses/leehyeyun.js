/**
 * @param {string} s
 * @return {boolean}
 */
/*
주어진 문자열 s는 괄호 문자로만 이루어져 있다.
사용 가능한 문자는 '(', ')', '{', '}', '[', ']' 총 6가지이다.

문자열이 올바른 괄호 문자열인지 판단하라.

올바른 괄호 문자열의 조건:
  1) 여는 괄호는 반드시 같은 종류의 닫는 괄호로 닫혀야 한다.
  2) 괄호는 올바른 순서로 닫혀야 한다.
     (가장 마지막에 열린 괄호가 가장 먼저 닫혀야 함)
  3) 모든 닫는 괄호는 대응되는 여는 괄호가 있어야 한다.

입력 형식 :
  - s: 문자열
  - 1 <= s.length <= 10,000
  - s는 '()[]{}' 문자로만 구성됨

출력 형식 :
  - 올바른 괄호 문자열이면 true
  - 그렇지 않으면 false

예시 :

  Example 1
    입력 : s = "()"
    출력 : true
    설명 :
      - '('가 ')'로 정상적으로 닫힘

  Example 2
    입력 : s = "()[]{}"
    출력 : true
    설명 :
      - 모든 괄호가 종류와 순서에 맞게 닫힘

  Example 3
    입력 : s = "(]"
    출력 : false
    설명 :
      - 여는 괄호 '('와 닫는 괄호 ']'의 종류가 다름

  Example 4
    입력 : s = "([])"
    출력 : true
    설명 :
      - 괄호가 중첩되어 있으나 순서와 종류 모두 올바름

  Example 5
    입력 : s = "([)]"
    출력 : false
    설명 :
      - 괄호의 닫히는 순서가 올바르지 않음
*/
var isValid = function (s) {
    const stack = [];

    for (var char of s) {
        if(char == "(" || char == "{" || char == "[")
        {
            stack.push(char);
        }else {
            const last = stack[stack.length - 1];
            if(char == ")" && last == "("){
                stack.pop();
            }else if (char == "}" && last == "{"){
                stack.pop();
            }else if (char == "]" && last == "["){
                stack.pop();
            }else {
                return false;
            }
        }
    }

    if(stack.length == 0)
    {
        return true;
    }else {
        return false
    }
};

console.log(isValid("()"))
console.log(isValid("()[]{}"))
console.log(isValid("(]"))
console.log(isValid("([])"))
console.log(isValid("([)]"))

