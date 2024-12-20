/**
 * 시간 복잡도:
 *   s와 t의 길이만큼 각 문자의 카운트를 기록하고 이를 확인하므로, 시간 복잡도는 O(n)
 * 공간 복잡도:
 *   카운트 객체는 최대 s와 t의 길이만큼 공간을 차지하므로, 공간 복잡도는 O(n)
 */
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) {
      return false;
  }

  const count = {};
  for (let i = 0; i < s.length; i++) {
      count[s[i]] = (count[s[i]] || 0) + 1;
      count[t[i]] = (count[t[i]] || 0) - 1;
  }

  for (const key in count) {
      if (count[key] !== 0) {
          return false;
      }
  }
  return true;
};
