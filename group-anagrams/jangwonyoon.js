/**
 * @param {string[]} strs
 * @return {string[][]}
 *
 * 시간 복잡도: O(n * mlogm)
 * 공간 복잡도: O(n * m)
 *
 */
var groupAnagrams = function(strs) {
    // 예외 처리
    if (strs.length === 1) return [[...strs]];

    const map = new Map();

    for (const str of strs) {
        const sortedStr = str.split('').sort().join('');
        if (!map.has(sortedStr)) map.set(sortedStr, []);
        map.get(sortedStr).push(str);
    }

    return [...map.values()];
};
