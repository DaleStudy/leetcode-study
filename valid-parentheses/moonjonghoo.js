/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let object = { ")": "(", "}": "{", "]": "[" };
  let stack = [];
  for (let char of s) {
    if (char === "(" || char === "{" || char === "[") {
      stack.push(char);
    } else {
      if (stack.length === 0 || stack.pop() !== object[char]) {
        return false;
      }
    }
  }
  return stack.length === 0;
};
