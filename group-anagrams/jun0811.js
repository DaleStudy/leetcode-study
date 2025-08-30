/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const hashMap = new Map();
  const res = [];
  strs.forEach((str, index) => {
    const sortedStr = [...str].sort().join('');
    if (hashMap.has(sortedStr)) {
      hashMap.set(sortedStr, [...hashMap.get(sortedStr), index]);
    } else {
      hashMap.set(sortedStr, [index]);
    }
  });
  for (const [key, values] of hashMap) {
    const anagrams = values.map((v) => strs[v]);
    res.push(anagrams);
  }
  return res;
};
