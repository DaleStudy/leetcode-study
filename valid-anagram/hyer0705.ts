function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const sCountMap = new Map<string, number>();
  const tCountMap = new Map<string, number>();

  for (let i = 0; i < s.length; i++) {
    const currentS = s[i];
    const currentT = t[i];

    sCountMap.set(currentS, (sCountMap.get(currentS) || 0) + 1);
    tCountMap.set(currentT, (tCountMap.get(currentT) || 0) + 1);
  }

  for (const [k, v] of sCountMap) {
    if (!tCountMap.has(k) || tCountMap.get(k) !== v) return false;
  }

  return true;
}
