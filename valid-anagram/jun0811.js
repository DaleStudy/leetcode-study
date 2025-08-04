/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

// Time Complexity : O(N)
var isAnagram = function (s, t) {
  if (s.length != t.length) return false;

  const hashMap = {};

  for (const chr of s) {
    if (chr in hashMap) {
      hashMap[chr] += 1;
    } else {
      hashMap[chr] = 1;
    }
  }

  for (const chr of t) {
    if (chr in hashMap && hashMap[chr] > 0) {
      hashMap[chr] -= 1;
    } else {
      return false;
    }
  }

  return true;
};
