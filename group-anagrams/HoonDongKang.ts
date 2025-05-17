/**
 * [Problem]: [49] Group Anagrams
 *
 * (https://leetcode.com/problems/group-anagrams/description/)
 */
function groupAnagrams(strs: string[]): string[][] {
    //시간복잡도 O(n * w log w)
    //공간복잡도 O(n * w)
    function mappedFunc(strs: string[]): string[][] {
        const map = new Map<string, string[]>();

        for (let str of strs) {
            let sorted = [...str].sort().join("");

            map.set(sorted, [...(map.get(sorted) ?? []), str]);
        }

        return [...map.values()];
    }

    //시간복잡오 O(n)
    //공간복잡도 O(n * w)
    function hashedMappedFunc(strs: string[]): string[][] {
        const map = new Map<string, string[]>();

        for (let str of strs) {
            const count: number[] = new Array(26).fill(0);

            for (const char of str) {
                count[char.charCodeAt(0) - 97]++;
            }

            const key = count.join("#");
            map.set(key, [...(map.get(key) ?? []), str]);
        }

        return [...map.values()];
    }
    return hashedMappedFunc(strs);
}
