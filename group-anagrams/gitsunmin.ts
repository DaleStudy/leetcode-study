/**
 * https://leetcode.com/problems/group-anagrams
 * time complexity : O(n * k log k)
 * space complexity : O(n * k)
 */
function groupAnagrams(strs: string[]): string[][] {
    const map = new Map();

    for (const str of strs) {
        const sortedStr = str.split("").sort().join("");

        if (map.has(sortedStr)) map.get(sortedStr).push(str);
        else map.set(sortedStr, [str]);
    }

    return Array.from(map.values());
};
