// n: length of strs, m: length of strs[i]
// Time complexity: O(nm)
// Space complexity: O(n)

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const answer = [];
  const anagramDict = new Map();

  const getKey = (str) => {
    const minCharCode = "a".charCodeAt();
    const maxCharCode = "z".charCodeAt();

    const counter = Array.from(
      { length: maxCharCode - minCharCode + 1 },
      () => 0
    );

    for (const chr of str) {
      const index = chr.charCodeAt() - minCharCode;
      counter[index]++;
    }

    return counter.join("#");
  };

  for (let i = 0; i < strs.length; i++) {
    const str = strs[i];
    const key = getKey(str);

    if (!anagramDict.has(key)) {
      anagramDict.set(key, []);
    }

    anagramDict.get(key).push(str);
  }

  for (const [_, value] of anagramDict) {
    answer.push(value);
  }

  return answer;
};
