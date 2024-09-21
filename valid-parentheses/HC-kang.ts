/**
 * https://leetcode.com/problems/valid-parentheses
 * T.C. O(n)
 * S.C. O(n)
 */
function isValid(s: string): boolean {
  const pairs: Record<string, string> = { '{': '}', '[': ']', '(': ')' };
  const stack: string[] = [];

  if (s.length % 2 == 1) return false;

  for (const char of s) {
    if (pairs[char]) stack.push(char);
    else if (char != pairs[stack.pop()!]) return false;
  }
  return !stack.length;
}
