/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = new Map()

    for(const str of strs) {
        const sortedStr = [...str].sort().join('')
        if(map.has(sortedStr)) {
            map.get(sortedStr).push(str)
        } else {
            map.set(sortedStr, [str])
        }
    }

    return Array.from(map.values())
};
