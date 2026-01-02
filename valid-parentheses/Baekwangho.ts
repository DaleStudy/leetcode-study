/**
 * 공간 복잡도: o(n) 시간 복잡도: o(n)
 */
function isValid(s: string): boolean {
  const stack = [];

  const start = ["(", "{", "["];

  for (let i = 0; i < s.length; i++) {
    if (start.includes(s[i])) {
      stack.push(s[i]);
    } else {
      const last = stack.pop();
      switch (last) {
        case "(": {
          if (s[i] !== ")") return false;
          break;
        }
        case "{": {
          if (s[i] !== "}") return false;
          break;
        }
        case "[": {
          if (s[i] !== "]") return false;
          break;
        }
        default: {
          return false;
        }
      }
    }
  }

  return stack.length > 0 ? false : true;
}
