function isAnagram(s: string, t: string): boolean {
  const obj = {};
  for (let i = 0; i < s.length; i++) {
    obj[s[i]] = (obj[s[i]] || 0) + 1;
  }

  for (let i = 0; i < t.length; i++) {
    obj[t[i]] -= 1;
  }

  return Object.values(obj).filter((value) => value !== 0).length === 0;
}
