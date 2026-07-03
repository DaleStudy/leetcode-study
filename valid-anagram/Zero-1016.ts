/**
 * 242. Valid Anagram
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 *
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 */
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const sMap = new Map<string, number>();
  const tMap = new Map<string, number>();

  // 문자열 s와 t를 순회하면서 각 문자의 빈도수를 계산
  for (let i = 0; i < s.length; i++) {
    sMap.set(s[i], (sMap.get(s[i]) || 0) + 1);
    tMap.set(t[i], (tMap.get(t[i]) || 0) + 1);
  }

  // 문자열 s와 t의 빈도수를 비교
  for (const [key, value] of sMap) {
    if (value !== tMap.get(key)) return false;
  }

  return true;
}
