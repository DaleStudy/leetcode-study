/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const sMap = new Map();
  const tMap = new Map();
  for (const str of [...s]) {
    sMap.set(str, (sMap.get(str) ?? 0) + 1);
  }

  for (const str of [...t]) {
    tMap.set(str, (tMap.get(str) ?? 0) + 1);
  }

  if (sMap.size === tMap.size) {
    let answer = true;
    for (let [str, count] of sMap) {
      if (!tMap.get(str) || tMap.get(str) !== sMap.get(str)) {
        answer = false;
      }
    }
    return answer;
  }

  return false;
};
