/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 * 
 * 시간복잡도 계산
 * 문자열 s 길이만큼 Map에 set => n
 * 문자열 t 길이만큼 Map에 set => n
 * 따라서 O(n)
 * 
 * 공간복잡도 계산
 * 문자열 s, t의 길이만큼 Map에 할당되니까 O(n)
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  const frequencyMap = new Map();

  for (const x of s) {
    frequencyMap.set(x, (frequencyMap.get(x) || 0) + 1);
  }

  for (const y of t) {
    if (!frequencyMap.has(y)) return false;
    frequencyMap.set(y, frequencyMap.get(y) - 1);
    if (frequencyMap.get(y) === 0) frequencyMap.delete(y);
  }

  return frequencyMap.size === 0;
};
