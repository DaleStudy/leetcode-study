/**
 *
 * @param s
 * @param t
 * @returns
 * 시간 복잡도 : O(n)
 * 공간 복잡도 : O(n)
 */
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const map = new Map<string, number>();

  for (let i = 0; i < s.length; i++) {
    map.set(s[i], (map.get(s[i]) ?? 0) + 1);
    map.set(t[i], (map.get(t[i]) ?? 0) - 1);
  }

  for (let ch of map.values()) {
    if (ch !== 0) {
      return false;
    }
  }

  return true;
}
