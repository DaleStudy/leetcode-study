// TC: O(N * log N)
// SC: O(N)

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  return s.split('').sort().join('') === t.split('').sort().join('');
};
