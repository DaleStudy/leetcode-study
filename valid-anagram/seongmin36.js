/**
결국 같아야 것은 string의 길이와 안에 들어간 각 character의 갯수다.
즉, s와 t의 문자의 갯수와 같으면 된다.
map을 사용하여 key와 value자리에 각각 문자, 갯수를 받는다.
s와 t를 비교하며 해당하는 문자 갯수-1을 한다.
각 key의 value를 문제없이 차감했다면 true를 반환. 그 외 false를 반환
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
function isAnagram(s, t) {
  if (s.length !== t.length) return false;

  let map_s = new Map();

  for (let char of s) {
    map_s.set(char, (map_s.get(char) || 0) + 1);
  }

  for (let char of t) {
    if (!map_s.has(char) || map_s.get(char) === 0) {
      return false;
    }
    map_s.set(char, map_s.get(char) - 1);
  }

  return true;
}
