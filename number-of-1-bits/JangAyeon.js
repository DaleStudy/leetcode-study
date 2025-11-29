/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  function calDivision(num) {
    return { v: Math.floor(num / 2), rest: num % 2 };
  }
  let num = n;
  let result = 0;
  while (true) {
    const { v, rest } = calDivision(num);
    result += rest;
    if (v == 0) {
      break;
    }
    num = v;
  }

  return result;
};
