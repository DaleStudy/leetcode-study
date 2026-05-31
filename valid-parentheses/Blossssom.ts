/**
 * @param s - 괄호 문자열
 * @returns - 올바르게 열고 닫혔는지 반환
 */
// function isValid(s: string): boolean {
//   const parentheses: Record<string, boolean> = {
//     "()": true,
//     "{}": true,
//     "[]": true,
//   };
//   const stack: string[] = [];
//   for (const st of s) {
//     if (
//       !stack.length ||
//       parentheses[`${stack[stack.length - 1]}${st}`] === undefined
//     ) {
//       stack.push(st);
//     } else {
//       stack.pop();
//     }
//   }
//   return stack.length ? false : true;
// }

function isValid(s: string): boolean {
  const parentheses: Record<string, string> = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  const stack: string[] = [];
  for (const char of s) {
    if (parentheses[char]) {
      stack.push(char);
    } else {
      const last = stack.pop();
      if (last === undefined || parentheses[last] !== char) {
        return false;
      }
    }
  }

  return !stack.length;
}


