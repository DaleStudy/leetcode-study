/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;
  let hashMap = new Map();
  for (let i = 0; i < s.length; i++) {
    if (hashMap.has(s[i])) {
      hashMap.set(s[i], hashMap.get(s[i]) + 1);
    } else {
      hashMap.set(s[i], 1);
    }
  }
  for (let i = 0; i < t.length; i++) {
    if (hashMap.has(t[i])) {
      hashMap.set(t[i], hashMap.get(t[i]) - 1);
      if (hashMap.get(t[i]) === 0) {
        hashMap.delete(t[i]);
      }
    }
  }

  if (hashMap.size === 0) return true;
  else return false;
};

isAnagram("anagram", "nagaram");
