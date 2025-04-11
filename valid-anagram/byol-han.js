/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  // 문자열 t를 배열로 변환해서 문자 제거할 수 있게 함
  let tArr = t.split("");

  for (let i = 0; i < s.length; i++) {
    let index = tArr.indexOf(s[i]); // s[i]가 tArr에 있는지 확인
    if (index === -1) {
      return false;
    }
    tArr.splice(index, 1);
  }
  return true;
};
