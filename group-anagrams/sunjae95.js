/**
 * @description
 * brainstorming:
 * brute force + hashtable
 *
 * time complexity: O(n* k log k)
 * space complexity: O(n* k)
 */
var groupAnagrams = function (strs) {
  const map = new Map();
  const answer = [];

  strs.forEach((str) => {
    const convertedStr = str.split("").sort().join();
    if (map.has(convertedStr))
      map.set(convertedStr, map.get(convertedStr).concat(str));
    else map.set(convertedStr, [str]);
  });

  map.forEach((value) => answer.push(value));

  return answer;
};
