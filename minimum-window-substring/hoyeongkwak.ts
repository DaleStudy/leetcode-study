/*
Time complexity: O(s+t)
Space complexity: O(s+t)
*/
function minWindow(s: string, t: string): string {
    const targetMap = new Map<string, number>()
    for (const char of t) {
        targetMap.set(char, (targetMap.get(char) || 0) + 1)
    }

    const requiredCnt = targetMap.size

    let left = 0
    let right = 0
    let formed = 0
    const windowCounts = new Map<string, number>()

    let minLen = Infinity
    let minLeft = 0
    let minRight = 0

    while (right < s.length) {
        const rightChar = s[right]
        windowCounts.set(rightChar, (windowCounts.get(rightChar) || 0) + 1)
        if (targetMap.has(rightChar) &&
            windowCounts.get(rightChar) === targetMap.get(rightChar)) {
            formed++
        }
    
        while (left <= right && formed == requiredCnt) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1
                minLeft = left
                minRight = right
            }
            const leftChar = s[left]
            windowCounts.set(leftChar, windowCounts.get(leftChar)! - 1)

            if (targetMap.has(leftChar) && windowCounts.get(leftChar)! < targetMap.get(leftChar)) {
                formed--
            }
            left++
        }
        right++
    }
    return minLen === Infinity ? "" : s.substring(minLeft, minRight + 1)
};
