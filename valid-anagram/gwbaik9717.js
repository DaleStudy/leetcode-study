// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const createDictFromString = (str) => {
    const dict = new Map();

    for (const chr of str) {
      if (dict.has(chr)) {
        dict.set(chr, dict.get(chr) + 1);
        continue;
      }

      dict.set(chr, 1);
    }

    return dict;
  };

  const dictS = createDictFromString(s);
  const dictT = createDictFromString(t);

  for (const [key, value] of dictS) {
    if (dictT.get(key) !== value) {
      return false;
    }
  }

  return true;
};
