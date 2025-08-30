// https://leetcode.com/problems/valid-parentheses
// Rumtime: 6ms
// Memory: 59.11MB

function isValid(s: string): boolean {
  let stack: string[] = [];

  for (let i = 0; i < s.length; i++) {
    if (["(", "{", "["].includes(s[i])) {
      stack.push(s[i]);
    } else {
      switch (s[i]) {
        case ")":
          if (stack.pop() !== "(") return false;
          break;
        case "}":
          if (stack.pop() !== "{") return false;
          break;
        case "]":
          if (stack.pop() !== "[") return false;
          break;
      }
    }
  }
  return stack.length === 0;
}
