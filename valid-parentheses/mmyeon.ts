/**
 *@link https://leetcode.com/problems/valid-parentheses/description/
 *
 * 접근 방법 :
 *  - 닫힌 괄호 나왔을 때 열린 괄호의 마지막 값과 짝이 맞는지 찾아야되니까 stack 사용
 *
 * 시간복잡도 : O(n)
 *  - 문자열 순회하면서 괄호체크하니까 O(n)
 *
 * 공간복잡도 : O(k)
 *  - pairs 객체 고정된 크기로 저장 O(1)
 *  - stack에 열린 괄호 개수만큼 담기니까 O(k)
 */

function isValid(s: string): boolean {
  const pairs: Record<string, string> = {
    ")": "(",
    "}": "{",
    "]": "[",
  };
  const stack: string[] = [];

  for (const char of s) {
    // 닫는 괄호 나온 경우 처리
    if (pairs[char]) {
      // 짝이 맞지 않는 경우
      if (stack[stack.length - 1] !== pairs[char]) return false;

      // 짝이 맞는 경우
      stack.pop();
    } else {
      // 열린 괄호는 바로 stack에 저장
      stack.push(char);
    }
  }

  return stack.length === 0;
}
