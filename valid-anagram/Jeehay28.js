/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

// 시간 복잡도: O(n)
// 공간 복잡도: O(n) 

var isAnagram = function (s, t) {

    if (s.length !== t.length) {
        return false;
    }

    let obj = {};

    for (let k of s) {
        obj[k] = (obj[k] || 0) + 1;

    }

    for (let k of t) {
        if (obj[k] === undefined || obj[k] === 0) {
            return false;
        }
        obj[k]--;
    }

    return true;

};

// 시간 복잡도: O(n log n)
// 공간 복잡도: O(n)

// var isAnagram = function (s, t) {

//     if (s.length !== t.length) {
//         return false;
//     }

//     let sArr = s.split("").sort();
//     let tArr = t.split("").sort();

//     for (let i = 0; i < sArr.length; i++) {
//         if (sArr[i] !== tArr[i]) {
//             return false;
//         }
//     }

//     return true;

// };

