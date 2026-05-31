function isValid(s: string): boolean {
  const stack = [];
  const open = '([{';
  for (const v of s) {
    if (open.includes(v)) {
      stack.push(v);
    } else {
      if (
        (v === ')' && stack.at(-1) === '(') ||
        (v === '}' && stack.at(-1) === '{') ||
        (v === ']' && stack.at(-1) === '[')
      ) {
        // 일치하는 닫는 괄호라면 pop
        stack.pop();
      } else {
        // 일치하지 않는 닫는 괄호라면 false
        return false;
      }
    }
  }

  return stack.length === 0 ? true : false;
}

function isValid(s: string): boolean {
  const pairs = new Map([
    [')', '('],
    ['}', '{'],
    [']', '['],
  ]);
  const stack = [];

  for (const v of s) {
    // v 가 닫는 괄호이면
    if (pairs.has(v)) {
      if (pairs.get(v) === stack.at(-1)) {
        // 일치하는 닫는 괄호라면 pop
        stack.pop();
      } else {
        // 일치하지 않는 닫는 괄호라면 false
        return false;
      }
    } else {
      // 여는 괄호이면
      stack.push(v);
    }
  }

  return stack.length === 0;
}

/*
1. 여는 괄호에 해당한다 -> 스택에 push
2. 닫는 괄호가 나왔다 -> 스택의 top과 일치하면 pop 아니라면 false
3. 스택이 비어있다 -> true
 */
