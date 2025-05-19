/*
    abc a l = 3
    bca b l = 3
    cab c l = 3
    abc b l = 1
    cb

    pw w l = 2
    wke w l = 3
    w
*/
/*
    time complexity : O(n)
    space complexity : O(n)
*/
function lengthOfLongestSubstring(s: string): number {
    if (s.length === 0) return 0

    let maxLen = 0
    let start = 0
    const charMap = new Map<string, number>()

    for (let end = 0; end < s.length; end++) {
        const currChar = s[end]

        if (charMap.has(currChar) && charMap.get(currChar)! >= start) {
            start = charMap.get(currChar)! + 1
        }
        charMap.set(currChar, end)
        maxLen = Math.max(maxLen, end - start + 1)
    }
    return maxLen
};
