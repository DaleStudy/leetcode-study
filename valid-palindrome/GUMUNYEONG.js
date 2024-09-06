/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {

    let str = normalize(s);
    let reverseStr = "";

    function normalize(str) {
        str = str.toLowerCase().replace(/[^a-z0-9]/g, "");

        return str;
    }


    for (let i = str.length - 1; i >= 0; i--) {
        reverseStr += str[i];
    };


    return str === reverseStr;
};

// TC : O(n)
// normalize 함수에서 n번(s의길이) 순회(toLowerCase) + n번 순회(replace)
// reverseStr 을 만들기 위해서 for문 - 길이 n 
// = O(3n) 따라서 O(n)

// SC : O(n)
// 변수 str , reversStr 모두 길이가 n 이므로 O(n)
