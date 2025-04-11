/**
 * O(n) time
 * O(문자수(s + t)) space
 */

function isAnagram(s: string, t: string): boolean {
  let sMap = new Map();
  let tMap = new Map();

  for (let i = 0; i < s.length; i++) {
    sMap.set(s[i], sMap.get(s[i]) + 1 || 1);
  }

  for (let i = 0; i < t.length; i++) {
    tMap.set(t[i], tMap.get(t[i]) + 1 || 1);
  }

  function areMapsEqual(map1, map2) {
    if (map1.size !== map2.size) return false;

    for (let [key, value] of map1) {
      if (map2.get(key) !== value) return false;
    }
    return true;
  }
  return areMapsEqual(sMap, tMap);
}
