/**
 * 20. Valid Parentheses
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 *
 * An input string is valid if:
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 * 3. Every close bracket has a corresponding open bracket of the same type.
 *
 * https://leetcode.com/problems/valid-parentheses/
 *
 */

// O(n^2) time
// O(1) space
function isValid(s: string): boolean {
  if (s.length % 2 === 1) return false;

  while (
    s.indexOf("()") !== -1 ||
    s.indexOf("{}") !== -1 ||
    s.indexOf("[]") !== -1
  ) {
    s = s.replace("()", "");
    s = s.replace("{}", "");
    s = s.replace("[]", "");
  }

  return s === "";
}
