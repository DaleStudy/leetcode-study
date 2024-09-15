/**
 * @param {string[]} strs
 * @return {string[][]}
 */

/**
 * Runtime: 100ms, Memory: 62.34MB
 * n = strs.length
 * k = 문자열의 최대 길이
 * Time complexity: O(n * k log k)
 * -> klogk는 길이가 k인 문자열을 sort
 * -> n은 이걸 각 문자열마다 반복하기 때문
 *
 * Space complexity: O(n)
 *
 */

var groupAnagrams = function (strs) {
  let answer = new Map();

  for (let j = 0; j < strs.length; j++) {
    const sortedWord = strs[j].split("").sort().join("");
    answer.has(sortedWord)
      ? answer.set(sortedWord, [...answer.get(sortedWord), strs[j]])
      : answer.set(sortedWord, [strs[j]]);
  }

  return Array.from(answer.values());
};
