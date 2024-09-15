// n 배열길이, k 단어길이
// 시간복잡도: O(n * k log k)
// 공간복잡도: O(n * k)
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = new Map()

    for (const word of strs) {
        const sortedWord = word.split("").sort().join("")

        if (!map.has(sortedWord)) {
            map.set(sortedWord, [])
        }

        map.set(sortedWord, [...map.get(sortedWord), word]);
    }


    return [...map.values()]
};

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
console.log(groupAnagrams([""]))
console.log(groupAnagrams(["a"]))
