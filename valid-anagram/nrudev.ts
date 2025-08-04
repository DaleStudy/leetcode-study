function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const sMap = new Map<string, number>();
  const tMap = new Map<string, number>();

  for (const letter of s) {
    if (sMap.has(letter)) sMap.set(letter, sMap.get(letter)!! + 1);
    else sMap.set(letter, 1);
  }

  for (const letter of t) {
    if (tMap.has(letter)) tMap.set(letter, tMap.get(letter)!! + 1);
    else tMap.set(letter, 1);
  }

  for (const [key, value] of sMap) {
    if (!tMap.has(key) || tMap.get(key) !== value) return false;
  }

  return true;
}
