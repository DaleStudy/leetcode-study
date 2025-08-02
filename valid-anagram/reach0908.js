/**
 * @description
 * time complexity: O(nlogn) split 시 새로운 배열을 생성하고 sort 시 nlogn 시간 소요
 * space complexity: O(n) split 시 새로운 배열을 생성함
 * runtime: 32ms
 * 풀이 방법: 두 문자열을 정렬하여 비교하는 방법
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function (s, t) {
  return s.split("").sort().join("") === t.split("").sort().join("");
};

/**
 * @description
 * time complexity: O(n)
 * space complexity: O(n)
 * runtime: 15ms
 * 풀이 방법: 해쉬맵을 통해 카운트를 추가하거나 제거하는 방식, 유니코드도 대응가능
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagramSolution2 = function (s, t) {
  if (s.length !== t.length) return false;

  const map = new Map();

  for (let i = 0; i < s.length; i += 1) {
    map.set(s[i], (map.get(s[i]) || 0) + 1);
    map.set(t[i], (map.get(t[i]) || 0) - 1);
  }

  for (const value of map.values()) {
    if (value !== 0) return false;
  }

  return true;
};
