/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

/**
 * Runtime: 68ms, Memory: 54.49MB
 * n = s.length > t.length ? s.length : t.length
 * Time complexity: O(n)
 * Space complexity: O(n)
 *
 * **/

function arrayToDict(arr) {
  const dict = {};
  for (let element of arr) {
    if (dict[element]) {
      dict[element] += 1;
    } else {
      dict[element] = 1;
    }
  }
  return dict;
}

function isSameDict(dict1, dict2) {
  if (Object.keys(dict1).length !== Object.keys(dict2).length) {
    return false;
  }

  for (const elem in dict1) {
    if (dict1[elem] !== dict2[elem]) {
      return false;
    }
  }
  return true;
}

var isAnagram = function (s, t) {
  const sArr = [...s];
  const tArr = [...t];

  const sDict = arrayToDict(sArr);
  const tDict = arrayToDict(tArr);

  return isSameDict(sDict, tDict);
};
