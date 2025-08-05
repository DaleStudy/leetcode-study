// leetCode 4기 답안
// /**
//  * @param {string} s
//  * @param {string} t
//  * @return {boolean}
//  */
// var isAnagram = function (s, t) {
//   let resultS = [...s].sort();
//   let resultT = [...t].sort();
//   return resultS.join() === resultT.join();
// };

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }

  // s를 돌면서 t에 있으면 제거
  let copyT = t;
  for (let i = 0; i < s.length; i++) {
    if (copyT.includes(s[i])) {
      copyT = copyT.replace(s[i], "");
    } else {
      return false;
    }
  }
  return true;
};
