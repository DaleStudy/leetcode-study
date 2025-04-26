/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  let resultS = [...s].sort();
  let resultT = [...t].sort();
  return resultS.join() === resultT.join();
};
