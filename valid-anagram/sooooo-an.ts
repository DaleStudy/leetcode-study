function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const objS: { [key: string]: number } = {};

  for (const str of s) {
    objS[str] = (objS[str] ?? 0) + 1;
  }

  for (const str of t) {
    if (!objS[str]) {
      return false;
    }
    objS[str]--;
  }

  return true;
}
