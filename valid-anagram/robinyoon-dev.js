/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    const counter = new Array(26).fill(0);

    //edge case: s와 t의 길이가 다른 경우
    if(s.length !== t.length) return false;

    for(let i = 0; i < s.length; i++){
        counter[s.charCodeAt(i) - 97]++;
        counter[t.charCodeAt(i) - 97]--;
    }

    return counter.every(count => count === 0);
};

