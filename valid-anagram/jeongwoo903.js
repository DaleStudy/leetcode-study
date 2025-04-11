/*
 * 시간 복잡도: O(n log n)
 * 공간 복잡도: O(n)
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  if(s.length !== t.length) return false;

  const strA = [...s].sort().join('');
  const strB = [...t].sort().join('');

  return strA === strB;
};
