/**
 * @param {string} s
 * @return {number}
 */

// TLE
// var numDecodings = function(s) {
//     const codeMap = {};
//     for (let i = 1; i <= 26; i++) {
//         codeMap[i] = String.fromCharCode(64 + i);
//     }

//     const memo = {};
//     let count = 0;
//     function go(string, start) {
//         if (start >= string.length) {
//             count++;
//             return;
//         }

//         const firstDigit = string[start];
//         const secondDigit = string[start + 1];
//         if (firstDigit === "0") return;

//         if (codeMap[firstDigit]) {
//             go(string, start + 1);
//         }

//         const twoDigits = firstDigit + secondDigit;
//         if (Number(twoDigits) <= 26 && codeMap[twoDigits]) {
//             go(string, start + 2);
//         }
//     }

//     go(s, 0, "");

//     return count;
// };

// TC: O(n) -> string 길이만큼
// SC: O(n) -> string 길이만큼 스택 생성
var numDecodings = function (s) {
  const codeMap = {};
  for (let i = 1; i <= 26; i++) {
    codeMap[i] = String.fromCharCode(64 + i);
  }

  const memo = {};

  function go(start) {
    if (start >= s.length) return 1;
    if (memo[start] !== undefined) return memo[start];

    const firstDigit = s[start];
    const secondDigit = s[start + 1];

    if (firstDigit === '0') return 0;

    let ways = 0;

    if (codeMap[firstDigit]) {
      ways += go(start + 1);
    }

    const twoDigits = firstDigit + secondDigit;
    if (Number(twoDigits) <= 26 && codeMap[twoDigits]) {
      ways += go(start + 2);
    }

    memo[start] = ways;

    return ways;
  }

  return go(0);
};
