// n: length of strs, m: length of strs[i]
// Time complexity: O(nmlogm)
// Space complexity: O(n)

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const answer = [];
  const anagramDict = new Map();

  const sortedStrs = strs.map((str) => {
    const splitted = str.split("");
    splitted.sort();
    return splitted.join("");
  });

  for (let i = 0; i < sortedStrs.length; i++) {
    const sortedStr = sortedStrs[i];
    const originalStr = strs[i];

    if (!anagramDict.has(sortedStr)) {
      anagramDict.set(sortedStr, []);
    }

    anagramDict.get(sortedStr).push(originalStr);
  }

  for (const [_, value] of anagramDict) {
    answer.push(value);
  }

  return answer;
};
