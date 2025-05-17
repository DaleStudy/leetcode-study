function isValid(s: string): boolean {
  const result: string[] = [];
  const open = ["(", "[", "{"];
  const close = [")", "]", "}"];
  for (let i = 0; i < s.length; i++) {
    if (open.includes(s[i])) {
      result.push(s[i]);
    } else {
      const index = close.findIndex((item) => item === s[i]);
      const popedItem = result.pop();
      if (popedItem !== open[index]) return false;
    }
  }
  return result.length === 0;
}
