/**
 * @description
 * brainstorming:
 * stack
 *
 * n: length of s
 * time complexity: O(n)
 * space complexity: O(n)
 */
var isValid = function (s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(" || s[i] === "{" || s[i] === "[") {
      stack.push(s[i]);
      continue;
    }

    const top = stack.length ? stack[stack.length - 1] : null;
    if (top === null) return false;

    if (
      (top === "(" && s[i] === ")") ||
      (top === "{" && s[i] === "}") ||
      (top === "[" && s[i] === "]")
    ) {
      stack.pop();
    } else return false;
  }

  return !stack.length;
};
