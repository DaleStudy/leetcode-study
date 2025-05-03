/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let hashMap = new Map();
  for (let i = 0; i < strs.length; i++) {
    let key = strs[i].split("").sort().join("");
    if (!hashMap.has(key)) {
      hashMap.set(key, [strs[i]]);
    } else {
      hashMap.set(key, [...hashMap.get(key), strs[i]]);
    }
  }
  let answer = [];
  for ([key, value] of hashMap) {
    answer.push(value);
  }
  return answer.sort((a, b) => a.length - b.length).map((arr) => arr.sort());
};

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
