/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const A_ASCII = 'a'.charCodeAt();

    const anagramMap = new Map();

    for (const str of strs) {
        const counter = new Array(26).fill(0);

        for (let i = 0; i < str.length; i++) {
            counter[str.charCodeAt(i) - A_ASCII]++;
        }

        let key = '';
        for (let i = 0; i < 26; i++) {
            if (counter[i] > 0) {
                key += String.fromCharCode(i + A_ASCII) + counter[i];
            }
        }

        if (!anagramMap.has(key)) {
            anagramMap.set(key, []);
        }
        anagramMap.get(key).push(str);
    }

    return Array.from(anagramMap.values());
};

// 시간 복잡도: O(n), 공간 복잡도: O(n)
