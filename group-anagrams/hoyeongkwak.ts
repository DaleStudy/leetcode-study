/* 
    time complexity : O(n * mlogm)
    space complexity : O(n * m)
*/
function groupAnagrams(strs: string[]): string[][] {
    const strMap = new Map<string, string[]>()
    for (let i = 0; i < strs.length; i++) {
        const sortedStr = strs[i].split('').sort().join('')
        if (!strMap.has(sortedStr)) {
            strMap.set(sortedStr, [strs[i]])
        } else {
            const prevArr = strMap.get(sortedStr)
            prevArr.push(strs[i])
            strMap.set(sortedStr, prevArr)
        }
    }
    return Array.from(strMap.values())
};
