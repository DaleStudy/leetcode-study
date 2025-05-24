function characterReplacement(s: string, k: number): number {
    /*

    */
    let maxLen = 0
    let maxCnt = new Map<string, number>()
    let start = 0
    let maxFreq = 0
    for (let e = 0; e < s.length; e++) {
        maxCnt.set(s[e], (maxCnt.get(s[e]) || 0) + 1)
        maxFreq = Math.max(maxFreq, maxCnt.get(s[e]))
        while (e - start + 1 - maxFreq > k) {
            maxCnt.set(s[start], maxCnt.get(s[start]) - 1)
            start += 1
        }
        maxLen = Math.max(e - start + 1, maxLen)
    }
    return maxLen
};
