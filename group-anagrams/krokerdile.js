/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const dict = new Map();

    strs.forEach(str => {
        const sorted = str.split('').sort().join('');
        if (!dict.has(sorted)) {
            dict.set(sorted, [str]);
        } else {
            dict.get(sorted).push(str);
        }
    });

    // value 길이 기준 내림차순 정렬
    const result = [...dict.entries()]
        .sort((a, b) => b[1].length - a[1].length)
        .map(([_, group]) => group); // value (즉, 아나그램 그룹)만 꺼냄

    return result;
};
