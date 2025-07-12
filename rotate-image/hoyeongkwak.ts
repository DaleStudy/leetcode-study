function longestPalindrome(s: string): string {
    if (s.length < 2) {
        return s
    }
    let maxStart = 0
    let maxEnd = 0
    for (let i = 0 ; i < s.length; i++) {
        let start = i
        let end = i
        while (0 <= start && end < s.length && s[start] === s[end]) {
            if (end - start > maxEnd - maxStart) {
                maxStart = start
                maxEnd = end
            }
            start--
            end++
        }

        start = i
        end = i + 1
        while (0 <= start && end <s.length && s[start] === s[end]) {
            if (end - start > maxEnd - maxStart) {
                maxStart = start 
                maxEnd = end
            }
            start--
            end++
        }
    }
    return s.slice(maxStart, maxEnd + 1)
};
