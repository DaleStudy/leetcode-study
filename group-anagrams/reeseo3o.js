/**
 * TC: O(n * k log k) — 각 단어(k) 정렬 × n개
 * SC: O(n * k)
 */
const groupAnagrams = (strs) => {
    const map = new Map();

    for (const str of strs) {
        const key = str.split("").sort().join("");

        if (!map.has(key)) {
            map.set(key, []);
        }

        map.get(key).push(str);
    }

    return Array.from(map.values());
};
