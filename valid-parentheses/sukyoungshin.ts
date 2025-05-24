const pairs = {
  ")": "(",
  "}": "{",
  "]": "[",
};

function isValid(s: string): boolean {
  const stack: string[] = [];
  for (let i = 0; i < s.length; i++) {
    const str = s[i];

    if (str in pairs) {
      if (pairs[str] !== stack[stack.length - 1]) {
        return false;
      } else {
        stack.pop();
      }
    } else {
      stack.push(str);
    }
  }

  return stack.length === 0;
};
