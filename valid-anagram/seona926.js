/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
let isAnagram = function (s, t) {
  let cntObj = {};

  s.split("").forEach((item) => {
    if (cntObj[item]) {
      ++cntObj[item];
    } else {
      cntObj[item] = 1;
    }
  });

  for (let item of t) {
    if (cntObj[item] === undefined || cntObj[item] < 1) {
      return false;
    } else {
      --cntObj[item];
    }
  }

  for (let count of Object.values(cntObj)) {
    if (count > 0) {
      return false;
    }
  }

  return true;
};
