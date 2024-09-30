// 시간복잡도: O(n)
// 공간복잡도: O(n)

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxCount = 0;
    const map = new Map()

    let leftIdx = 0;
    for (let rightIdx = 0 ; rightIdx < s.length; rightIdx++) {
        const char = s[rightIdx]
        if (map.has(char) && map.get(char) >= leftIdx) leftIdx = map.get(char) + 1;
        map.set(char, rightIdx)
        maxCount = Math.max(maxCount, rightIdx - leftIdx + 1)
    }

    return maxCount
};


console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("bbbbb"))
console.log(lengthOfLongestSubstring("pwwkew"))
console.log(lengthOfLongestSubstring("abba"))

