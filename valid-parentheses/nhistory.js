/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  // Create stack array
  let stack = [];
  // Iterate string to find there is an open bracket
  for (char of s) {
    // If it is an open bracket, push the close bracket into stack array
    if (char === "(") stack.push(")");
    else if (char === "{") stack.push("}");
    else if (char === "[") stack.push("]");
    // If it is not an open bracket, compare last element of stack array
    else if (char !== stack.pop()) return false;
  }
  // Check stack array still has any element after iteration
  return stack.length === 0;
};

// TC: O(n)
// MC: O(n)

console.log(isValid("()")); //true
console.log(isValid("()[]{}")); //true
console.log(isValid("([)]")); //false
