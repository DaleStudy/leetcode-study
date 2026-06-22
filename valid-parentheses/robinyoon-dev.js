/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const bracketsObj = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    const stackArray = [];

    for (let i = 0; i < s.length; i++) {

        let currentBracket = s[i];
        let isRightBracket = currentBracket in bracketsObj;

        if (!isRightBracket) {
            stackArray.push(currentBracket);
            continue;
        }

        let isPair = stackArray[stackArray.length - 1] == bracketsObj[currentBracket];

        if (isPair) {
            stackArray.pop();
        } else {
            return false;
        }
    }

    return stackArray.length === 0

};


// -----6기 활동 시의 풀이----
// /**
//  * @param {string} s
//  * @return {boolean}
//  */
// var isValid = function (s) {

//     const tempArray = [];
//     const pairObject = {
//         ')': '(',
//         '}': '{',
//         ']': '['
//     }

//     for (const ch of s) {
//         if (ch === '(' || ch === '{' || ch === '[') {
//             tempArray.push(ch);
//         } else {
//             if (tempArray.pop() !== pairObject[ch]) {
//                 return false;
//             }
//         }
//     }

//     return tempArray.length === 0;
// };



