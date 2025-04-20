/* 
    time complexity : O(n)
    space complexity : O(n)
*/
function numDecodings(s: string): number {
    const memo = new Map<number, number>()
    const decode = (index: number): number => {
        if (index === s.length) return 1
        if (s[index] === '0') return 0
        if (memo.has(index)) return memo.get(index)
        
        let ways = decode(index + 1)
        if (index + 1 < s.length && (s[index] === '1' || (s[index] === '2' && parseInt(s[index + 1]) <= 6))) {
            ways += decode(index + 2)
        }
        memo.set(index, ways)
        return ways
    }
    return decode(0)
}