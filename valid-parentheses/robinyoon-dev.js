/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {

    const tempArray = [];
    const pairObject = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for (const ch of s) {
        if (ch === '(' || ch === '{' || ch === '[') {
            tempArray.push(ch);
        } else {
            if (tempArray.pop() !== pairObject[ch]) {
                return false;
            }
        }
    }

    return tempArray.length === 0;
};


