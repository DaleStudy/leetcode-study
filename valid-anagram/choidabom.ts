/**
 * Runtime: 24ms, Memory: 55.95MB
 *
 * 접근: 문자들끼리 anagram 관계인 경우, 정렬했을 때 같은 값을 가지기에 각 문자열 정렬 후 비교.
 */

function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }
  return sortedString(s) === sortedString(t);
}

function sortedString(s: string): string {
  return s.split("").sort().join("");
}

/**
 * Runtime: 29ms, Memory: 55.02MB
 *
 * 접근: 문자들끼리 anagram 관계인 경우, 각 문자들의 count가 동일할 것이기에 Map 자료구조를 이용해서 합/차 계산
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  let map = new Map<string, number>();
  for (const char of s) {
    if (map.has(char)) {
      map.set(char, map.get(char)! + 1);
    } else {
      map.set(char, 1);
    }
  }

  for (const char of t) {
    if (map.has(char)) {
      map.set(char, map.get(char)! - 1);
    } else {
      return false;
    }
  }

  for (const value of map.values()) {
    if (value !== 0) {
      return false;
    }
  }

  return true;
}

console.log(isAnagram("anagram", "nagaram"));
