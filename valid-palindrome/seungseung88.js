/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
// var isPalindrome = function (s) {
//   // 숫자와 문자만 추출하는 정규식
//   const REGEX = /[0-9a-zA-Z]/g;

//   const wordArr = s.match(REGEX);

//   // 문자가 비어있으면 true반환
//   if (!wordArr) return true;

//   let l = 0;
//   let r = wordArr.length - 1;

//   while (l < r) {
//     if (wordArr[l].toLocaleLowerCase() !== wordArr[r].toLocaleLowerCase()) return false;
//     console.log(l, r);
//     l += 1;
//     r -= 1;
//   }

//   return true;
// };

/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: 1
 */
var isPalindrome = function (s) {
  // 숫자와 문자만 추출하는 정규식
  const isAlnum = (char) =>
    (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') || (char >= '0' && char <= '9');

  let l = 0;
  let r = s.length - 1;

  while (l < r) {
    console.log(l, r);
    if (!isalnum.test(s[l])) {
      l += 1;
      continue;
    }
    if (!isalnum.test(s[r])) {
      r -= 1;
      continue;
    }
    if (s[l].toLowerCase() !== s[r].toLowerCase()) {
      return false;
    }
    l += 1;
    r -= 1;
  }

  return true;
};

const s = 'A man, a plan, a canal: Panama';

console.log(isPalindrome(s));
