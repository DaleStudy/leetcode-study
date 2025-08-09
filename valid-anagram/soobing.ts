/**
 * 문제 유형
 * - String
 *
 * 문제 설명
 * - 두 문자열이 애너그램인지 확인하기
 *
 * 아이디어
 * 1) 문자열을 맵으로 변환하고, 정렬 후 비교하기
 * 2) 문자열 정렬 없이 하나의 map으로 더하고 빼기하여 0인지 확인하기
 */
function mapString(str: string) {
  const map = new Map<string, number>();
  for (let i = 0; i < str.length; i++) {
    map.set(str[i], (map.get(str[i]) || 0) + 1);
  }
  return map;
}
function isAnagram(s: string, t: string): boolean {
  const sMap = mapString(s);
  const tMap = mapString(t);

  const sKeys = [...sMap.keys()].sort().join("");
  const tKeys = [...tMap.keys()].sort().join("");

  if (sKeys !== tKeys) return false;

  for (let i = 0; i < sKeys.length; i++) {
    const key = sKeys[i];
    if (sMap.get(key) !== tMap.get(key)) return false;
  }

  return true;
}

// 아이디어 2
function isAnagramDeveloped(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const count = new Map<string, number>();

  for (let i = 0; i < s.length; i++) {
    count.set(s[i], (count.get(s[i]) || 0) + 1);
    count.set(t[i], (count.get(t[i]) || 0) - 1);
  }

  for (const val of count.values()) {
    if (val !== 0) return false;
  }

  return true;
}
