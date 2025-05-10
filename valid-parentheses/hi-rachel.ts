// TC: O(N^2), SC: O(N)
// function isValid(s: string): boolean {
//   let prevLength = -1;

//   while (s.length !== prevLength) {
//     prevLength = s.length;
//     s = s.replace("()", "").replace("[]", "").replace("{}", "");
//   }

//   return s.length === 0;
// }

/**
 * STACK 풀이
 * TC: O(N), SC: O(N)
 * 스택 방식 작동 순서
* for (const char of s) {
  if (여는 괄호) {
    스택에 push
  } else {
    스택에서 pop한 값이 char의 짝이 아니면 return false
  }
}
 */
function isValid(s: string): boolean {
  const stack: string[] = [];
  const parentheseMap: Record<string, string> = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  for (const char of s) {
    if (["(", "[", "{"].includes(char)) {
      stack.push(char);
    } else {
      if (stack.pop() !== parentheseMap[char]) return false;
    }
  }
  return stack.length === 0;
}

/**
 * Python과 JS에서의 pop() 메서드 차이
 * JS 같은 로직을 Python으로 바꾸면 Python에서만 다음과 같은 테스트 케이스 오류가 발생
 * TEST CASE: "]", "){", ")(){}"
 *
 * [원인]
 * if (stack.pop() !== parentheseMap[char]) return false; 비교시
 * JavaScript에서는 빈 스택 pop() -> undefined 반환으로 비교 가능!
 * Python에서는 빈 스택 pop() -> IndexError -> 오류 발생
 *
 * [해결책] - 예외 처리 필요
 * pop 전에 not stack 체크 꼭 해주기
 * not stack -> 스택이 비어 있다면 잘못된 닫는 괄호 먼저 나온 경우
 */

// PY 풀이
// class Solution:
//     def isValid(self, s: str) -> bool:
//         parentheseMap = {")" : "(", "]": "[", "}": "{"}
//         stack = []
//         open_parenthese = "([{"

//         for char in s:
//             if char in open_parenthese:
//                 stack.append(char)
//             else:
//                 if (not stack or stack.pop() != parentheseMap[char]):
//                     return False

//         return len(stack) == 0
