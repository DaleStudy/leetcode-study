/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {

    let str = newStr(s);
    let reverseStr = "";

    function newStr(str) {
        str = str.toLowerCase().replace(/[^a-z0-9]/g, "");

        return str;
    }


    for (let i = str.length - 1; i >= 0; i--) {
        reverseStr += str[i];
    };


    return str === reverseStr;
};
