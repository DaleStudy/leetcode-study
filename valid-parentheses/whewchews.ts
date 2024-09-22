/*
 * 아이디어
 * stack 자료구조를 사용해 여는 괄호가 나오면 순서대로 저장해둔다.
 * stack을 사용하는 이유는 가장 최근 여는 괄호가 어떤 것인지 확인하기 위함이다.(마지막에 삽입한 값을 먼저 사용함)
 * 닫는 괄호가 나오면 stack의 마지막 값이 pair인 여는 괄호인지 체크한다. 다르면 return false
 * 문자열 반복문을 다 돌고 stack에 여는 괄호가 남아있지 않은지 본다. 남아있으면 return false
 * 위의 두 경우에 해당되지 않으면 return true
 */
function isValid(s: string): boolean {
  const openCharStack = [];
  const CHAR_PAIR = {
    "]": "[",
    "}": "{",
    ")": "(",
  };

  for (let i = 0; i <= s.length - 1; i++) {
    const char = s[i];

    if (char in CHAR_PAIR) {
      const pair = CHAR_PAIR[char];
      const lastOpenChar = openCharStack.pop();
      if (lastOpenChar !== pair) {
        return false;
      }
    } else {
      openCharStack.push(char);
    }
  }

  const isEmpty = openCharStack.length === 0;
  return isEmpty;
}
// TC: O(n)
// SC: O(n)
