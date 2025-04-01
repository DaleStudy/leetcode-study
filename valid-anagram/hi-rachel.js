/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  let hashMap1 = new Map();
  let hashMap2 = new Map();

  for (let i = 0; i < s.length; i++) {
    hashMap1.set(s[i], (hashMap1.get(s[i]) || 0) + 1);
  }

  for (let i = 0; i < t.length; i++) {
    hashMap2.set(t[i], (hashMap2.get(t[i]) || 0) + 1);
  }

  function areMapsEqual(map1, map2) {
    if (map1.size !== map2.size) return false;

    for (let [key, value] of map1) {
      if (map2.get(key) !== value) return false;
    }
    return true;
  }
  return areMapsEqual(hashMap1, hashMap2);
};
