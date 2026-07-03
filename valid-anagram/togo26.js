/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
// TC: O(nlogn) / SC: O(n)
var isAnagram = function (s, t) {
  const sortedS = [...s].sort().join('');
  const sortedT = [...t].sort().join('');
  return sortedS === sortedT;
};

// TC: O(n) / SC: O(n)
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;
  const sCount = [...s].reduce((acc, cur) => {
    acc[cur] = acc[cur] + 1 || 1;
    return acc;
  }, {});
  const tCount = [...t].reduce((acc, cur) => {
    acc[cur] = acc[cur] + 1 || 1;
    return acc;
  }, {});
  return Object.keys(sCount).every(key => sCount[key] === tCount[key]);
};
