/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const stringMap = new Map();

  if (s.length !== t.length) return false;

  for (let i = 0; i < s.length; i++) {
    const currentValue = stringMap.get(s[i]);

    if (currentValue) {
      stringMap.set(s[i], currentValue + 1);
    } else {
      stringMap.set(s[i], 1);
    }
  }

  for (let i = 0; i < t.length; i++) {
    const currentValue = t[i];
    const currentValueInStringMap = stringMap.get(currentValue);

    if (currentValueInStringMap) {
      stringMap.set(currentValue, currentValueInStringMap - 1);
    } else {
      return false;
    }
  }

  return true;
};
