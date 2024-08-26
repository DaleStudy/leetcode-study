// TC: O(N)
// SC: O(N)

/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  if (s[0] === "0") {
    return 0;
  }
  if (s.length === 1) {
    return 1;
  }

  const dpTable = new Array(s.length).fill(0);
  if (s[0] !== "0") {
    dpTable[0] = 1;
  }
  if (s[1] !== "0") {
    dpTable[1] += 1;
  }
  if (isValid(`${s[0]}${s[1]}`)) {
    dpTable[1] += 1;
  }

  for (let index = 2; index < s.length; index++) {
    if (s[index] !== "0") {
      dpTable[index] += dpTable[index - 1];
    }
    if (s[index - 1] !== "0" && isValid(`${s[index - 1]}${s[index]}`)) {
      dpTable[index] += dpTable[index - 2];
    }
  }

  return dpTable[dpTable.length - 1];

  function isValid(stringNumber) {
    const number = Number(stringNumber);
    if (number <= 0) {
      return false;
    }
    if (27 <= number) {
      return false;
    }
    return true;
  }
};
