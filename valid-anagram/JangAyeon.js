/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const sCounter = new Map();
  for (let e of s) {
    // console.log(e)
    const value = sCounter.has(e) ? sCounter.get(e) + 1 : 1;
    sCounter.set(e, value);
  }
  console.log(sCounter);

  for (let e of t) {
    if (!sCounter.has(e)) {
      return false;
    }
    const value = sCounter.get(e);
    if (value - 1 < 0) {
      return false;
    }
    if (value - 1 == 0) {
      sCounter.delete(e);
    } else {
      sCounter.set(e, value - 1);
    }
  }
  const notAllused = [...sCounter.keys()].length;
  return !notAllused;
};
