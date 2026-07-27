/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const pairs = { ")": "(", "]": "[", "}": "{" };
  const stack = [];

  for (const ch of s) {
    if (!pairs[ch]) {
      stack.push(ch);
      continue;
    }

    if (stack.pop() !== pairs[ch]) {
      return false;
    }
  }

  return stack.length === 0;
};
