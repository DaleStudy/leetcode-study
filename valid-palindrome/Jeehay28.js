/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const reg = /[a-z0-9]/g;
  const converted = s.toLowerCase().match(reg);

  if (converted === null) {
    return true;
  } else {
    const forward = converted.join("");
    const backward = converted.reverse().join("");

    return forward === backward;
  }
};
