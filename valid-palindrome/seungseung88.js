/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  // 숫자와 문자만 추출하는 정규식
  const REGEX = /[0-9a-zA-Z]/g;

  const wordArr = s.match(REGEX);

  // 문자가 비어있으면 true반환
  if (!wordArr) return true;

  let l = 0;
  let r = wordArr.length - 1;

  while (l < r) {
    if (wordArr[l].toLocaleLowerCase() !== wordArr[r].toLocaleLowerCase()) return false;
    console.log(l, r);
    l += 1;
    r -= 1;
  }

  return true;
};
