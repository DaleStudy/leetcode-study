/**
 * Complexity:
 * - Time: O(n)
 * - Space:	O(n)
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  const freqS = new Map();
  const freqT = new Map();

  for (let i = 0; i < s.length; i++) {
    freqS.set(s[i], (freqS.get(s[i]) || 0) + 1);
    freqT.set(t[i], (freqT.get(t[i]) || 0) + 1);
  }

  if (freqS.size !== freqT.size) return false;

  for (const [key, value] of freqS) {
    if (freqT.get(key) !== value) return false;
  }

  return true;
};
