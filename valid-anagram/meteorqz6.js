// 시간 복잡도: O(n log n)
// 공간 복잡도: O(n)

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const sortS = s.split("").sort().join("");
  const sortT = t.split("").sort().join("");

  if (sortS === sortT) return true;
  else return false;
};
