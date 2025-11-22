/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
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
