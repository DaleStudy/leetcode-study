// Time Complexity: O(n)
// Space Complexity: O(n)

function isValid(s: string): boolean {
  const map = new Map<string, string>([
    ["(", ")"],
    ["{", "}"],
    ["[", "]"],
  ]);

  let stack: string[] = [];

  for (const ch of s) {
    if (map.has(ch)) {
      stack.push(ch);
    } else {
      const last = stack.pop();
      if (!last || ch !== map.get(last)) {
        return false;
      }
    }
  }

  return stack.length === 0;
}

