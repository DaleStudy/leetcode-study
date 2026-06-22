/*
스택을 만들어 s를 탐색하며 집어넣고, 허용되지 않은 괄호가 오면 false를 리턴한다
- 허용하는 괄호 : 열려있는 괄호 (, {, [ 혹은 마지막 원소의 짝이 되는 닫는괄호

시간복잡도 : O(N) - N은 s의 length
공간복잡도 : O(N) (괄호 배열 및 괄호 쌍)
*/

function isValid(s: string): boolean {
  const stack = []
  const openBrackets = ['(', '{', '[']
  const bracketMap = {
    '(': ')',
    '{': '}',
    '[': ']',
  }

  for (const char of s) {
    if (openBrackets.includes(char)) {
      stack.push(char)
      continue
    }
    const last = stack.at(-1)
    if (char === bracketMap[last]) {
      stack.pop()
      continue
    }

    return false
  }

  return stack.length === 0
}
