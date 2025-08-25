/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const match = {
    ')': '(',
    ']': '[',
    '}': '{',
  };
  if (match[s[0]]) return false;
  const stack = [];
  for (const bracket of s) {
    if (bracket == '(' || bracket == '{' || bracket == '[') stack.push(bracket);
    else {
      const openBracket = stack.pop();
      if (match[bracket] != openBracket) return false;
    }
  }
  if (stack.length > 0) return false;
  return true;
};
