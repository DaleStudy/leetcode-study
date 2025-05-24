/**
 * 회문인 부분 문자열의 개수를 반환하는 함수
 * @param {string} s
 * @return {number}
 */
const countSubstrings = function(s) {
    let count = 0;

    for (let i = 0; i <s.length; i++) {
        let substr = '';
        let reversed = '';

        for (let j = i; j < s.length; j++){
            substr += s[j];
            reversed = s[j] + reversed;
            if (substr === reversed) {
                count += 1;
            }
        }
    }

    return count;
};

// 시간복잡도: O(n^2)
// 공간복잡도: O(n)
