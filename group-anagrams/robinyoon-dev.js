/**
 * @param {string[]} strs
 * @return {string[][]}
 */

// 문제는 풀었으나 시간 복잡도 측면에서 효율이 너무 떨어지는 풀이 방법....
var groupAnagrams = function (strs) {
    let outputArr = [];
    let countArr = [];

    const A_ASCII = 'a'.charCodeAt(0);
    const Z_ASCII = 'z'.charCodeAt(0);

    let charCounts = Z_ASCII - A_ASCII + 1;
    let charCountArr = new Array(charCounts).fill(0); //인덱스가 알파벳을 나타냄.

    for (str of strs) {
        let strCountString = getStrCountString(str);

        let hasSameCountIndex = countArr.findIndex((item) => item === strCountString);

        if (hasSameCountIndex !== -1) {
            outputArr[hasSameCountIndex].push(str);
        } else {
            countArr.push(strCountString);

            outputArr.push([str]);
        }
    }

    return outputArr;

    function getStrCountString(str) {
        let tempArr = [...charCountArr];

        for (char of str) {
            let charAscii = char.charCodeAt(0);
            let charIndex = charAscii - A_ASCII;
            tempArr[charIndex] += 1;
        }
        return tempArr.join(',');
    }
};


