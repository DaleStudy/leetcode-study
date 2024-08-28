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

/*
  1. 시간복잡도 : O(n)
  각 반복문의 시간복잡도가 모두 O(n)

  2. 공간복잡도 : O(n)
  주어진 문자열인 s와 t갯수만큼 공간을 차지함
*/

