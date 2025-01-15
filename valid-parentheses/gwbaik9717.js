// n: len(s)
// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];

  for (const chr of s) {
    if (
      (stack.at(-1) === "(" && chr === ")") ||
      (stack.at(-1) === "{" && chr === "}") ||
      (stack.at(-1) === "[" && chr === "]")
    ) {
      stack.pop();
      continue;
    }

    stack.push(chr);
  }

  return stack.length === 0;
};
