function isValid(s: string): boolean {
  const stack: string[] = [];

  const matchMap = new Map<string, string>();
  matchMap.set(")", "(");
  matchMap.set("]", "[");
  matchMap.set("}", "{");

  for (const bracket of s) {
    if (matchMap.has(bracket)) {
      if (stack.length === 0 || matchMap.get(bracket) !== stack.pop()) {
        return false;
      }
    } else {
      stack.push(bracket);
    }
  }

  return stack.length === 0;
}
