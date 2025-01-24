/**
 * @param {string} s
 * @return {boolean}
 */

// Time Complexity: O(n)
// Space Complexity: O(n)
var isValid = function (s) {
  const obj = {
    "(" : ")",
    "{" : "}",
    "[" : "]",
  };

  let stack = [];

  for (any of s) {
    // open bracket
    if (obj[any]) {
      stack.push(any);
    } else {
      // close bracket
      if (stack.length === 0) {
        return false;
      } else if (obj[stack[stack.length - 1]] !== any) {
        return false;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length === 0 ? true : false;
};


