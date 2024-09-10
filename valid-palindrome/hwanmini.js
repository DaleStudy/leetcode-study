// 시간복잡도: O(n)
// 공간복잡도: O(n)

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const strs = s.replace(/[^a-z0-9]/gi, '').toLowerCase();

    let leftIdx = 0;
    let rightIdx = strs.length - 1

    while (leftIdx <= rightIdx) {
        if (strs[leftIdx] !== strs[rightIdx]) return false

        leftIdx++
        rightIdx--
    }


    return true
};

const s = "A man, a plan, a canal: Panama"


console.log(isPalindrome(s))

