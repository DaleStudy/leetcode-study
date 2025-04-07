function isAnagram(s: string, t: string): boolean {
  const map = new Map();
  for (let i = 0; i < s.length; i++) {
    map.set(s[i], (map.get(s[i]) || 0) + 1);
  }
  for (let i = 0; i < t.length; i++) {
    if (!map.has(t[i])) {
      return false;
    }
    const newCount = map.get(t[i]) - 1;
    if (newCount < 0) return false;
    if (newCount === 0) map.delete(t[i]);
    else map.set(t[i], map.get(t[i]) - 1);
  }

  return map.size === 0;
}
