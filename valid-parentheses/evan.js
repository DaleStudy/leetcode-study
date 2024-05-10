/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  if (s.length % 2 !== 0) {
    return false;
  }

  const stack = [];
  const pair = {
    ")": "(",
    "}": "{",
    "]": "[",
  };

  for (let char of s) {
    if (pair[char] && stack.pop() !== pair[char]) {
      return false;
    }

    stack.push(char);
  }

  return stack.length === 0;
};
