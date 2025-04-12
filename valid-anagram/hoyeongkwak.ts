function isAnagram(s: string, t: string): boolean {
    // 시간복잡도 O(nlogn), 공간복잡도 O(n)
    // const sSorted = s.split('').sort().join(',')
    // const tSorted = t.split('').sort().join(',')
    // return sSorted === tSorted

    /*
    시간복잡도 O(n), 공간복잡도 O(1)
    */
    if (s.length != t.length) return false
    const count = new Array(26).fill(0)
    for (let i = 0; i < s.length; i++) {
        count[s.charCodeAt(i) - 97]++
        count[t.charCodeAt(i) - 97]--
    }
    return count.every(c => c === 0)
};