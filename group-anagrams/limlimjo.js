/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  // map에 담기
  const map = new Map();

  // for문 돌기
  for (const str of strs) {
    // 정렬된 단어
    const sortWord = str.split("").sort().join("");
    // map에 가지고 있지 않을 때
    if (!map.has(sortWord)) {
      map.set(sortWord, []);
    }
    map.get(sortWord).push(str);
  }

  return Array.from(map.values());
};
