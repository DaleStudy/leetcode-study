/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  /*
    // Split string and sort charaters
    // Compare s and t after sorting
    return s.split("").sort().join() === t.split("").sort().join()
    // 92ms, 53.29MB
    */

  // Made Hashmap and count number of each charater
  let map = {};

  // Check character length between s and t
  if (s.length !== t.length) return false;
  // Put a character and add or substract number
  for (let i = 0; i < s.length; i++) {
    // map[s[i]] = map[s[i]] ? map[s[i]] + 1 : 1;
    map[s[i]] = (map[s[i]] ?? 0) + 1;
    // map[t[i]] = map[t[i]] ? map[t[i]] - 1 : -1;
    map[t[i]] = (map[t[i]] ?? 0) - 1;
  }

  for (let i = 0; i < s.length; i++) {
    if (map[s[i]] !== 0) return false;
  }

  return true;
};

console.log(isAnagram("anagram", "nagaram"));
console.log(isAnagram("rat", "car"));

// TC: O(n)
// SC: O(n)
