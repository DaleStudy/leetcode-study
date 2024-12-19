/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // 1. 문자열을 다 소문자로 바꾸고, 알파벳/숫자 아닌 거 다 제거
    if (s.length === 1) {
        return true;
    } else {
        let lcLetter = s.toLowerCase().replace(/[^a-z0-9]/g, '');
        //console.log(lcLetter);

        // 2. 문자열이 앞에서 시작할 때와 뒤에서 시작할 때 같으면 true, 아니면 false
        if(lcLetter) {
            for(let i=0; i<Math.floor(lcLetter.length/2); i++) {
                if (lcLetter[i] !== lcLetter[lcLetter.length - 1 - i]) return false;
            }
            return true;
        } else {
            return true;
        }
    }
};
