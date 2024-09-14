/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let map = new Map();

  for (let str of strs) {
    let sortedStr = str.split('').sort().join('');

    if (map.has(sortedStr)) {
      map.get(sortedStr).push(str);
    } else {
      map.set(sortedStr, [str]);
    }
  }

  return Array.from(map.values());
};

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
console.log(groupAnagrams([""]));
console.log(groupAnagrams(["a"]));


/*
시간 복잡도: O(n*k log k)
공간 복잡도: O(n*k)

n: 문자열의 개수
k: 문자열의 최대 길이
*/
