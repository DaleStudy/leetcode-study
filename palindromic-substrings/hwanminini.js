// 시간 복잡도: O(n^3)
// 공간 복잡도: O(1)

/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let count = 0;

    let plusIndex = 0;
    while (plusIndex !== s.length) {
        for (let i = 0 ; i < s.length - plusIndex; i++) {
            if (isValidSubstring(s, i, i + plusIndex)) count++
        }

        plusIndex++;
    }

    return count;
};


function isValidSubstring(s, left, right) {
    while (left <= right) {
        if (s[left] !== s[right]) return false;

        left++;
        right--;
    }
    return true;
}

console.log(countSubstrings("abc"));
console.log(countSubstrings("aaa"));
