/**
 * 주어진 문자열이 조건을 만족하는 회문인지 여부를 반환하는 함수
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function(s) {
    const filtered = Array.from(s.toLowerCase()).reduce((str, char) => {
        return isAlphanumeric(char) ? str + char : str;
    }, '');

    for (let left = 0, right = filtered.length - 1; left < right; left++, right--) {
        if (filtered[left] !== filtered[right]) {
            return false;
        }
    }

    return true;
};


function isAlphanumeric(char) {
    return char !== ' ' && (('a' <= char && char <= 'z') || !Number.isNaN(Number(char)));
}

// 시간복잡도: O(n)
// 공간복잡도: O(n)
