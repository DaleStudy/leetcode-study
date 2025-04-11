/**
 * [Problem]: [242] Valid Anagram
 * (https://leetcode.com/problems/valid-anagram/description/
 */
function isAnagram(s: string, t: string): boolean {
    // 시간복잡도: O(nlogn)
    // 공간복잡도: O(n)
    function sortJoinFunc(s: string, t: string): boolean {
        return [...s].sort().join() === [...t].sort().join();
    }

    // 시간복잡도: O(n)
    // 공간복잡도: O(n)
    function asciiDiffFunc(s: string, t: string): boolean {
        if (s.length !== t.length) return false;

        const asciiMap = new Map<string, number>();
        for (let i = 0; i < s.length; i++) {
            const sChar = s[i];
            const tChar = t[i];

            asciiMap.set(sChar, (asciiMap.get(sChar) || 0) + 1);
            asciiMap.set(tChar, (asciiMap.get(tChar) || 0) - 1);
        }

        for (const count of asciiMap.values()) {
            if (count !== 0) return false;
        }

        return true;
    }

    // 시간복잡도: O(n)
    // 공간복잡도: O(1)
    function arrayFunc(s: string, t: string): boolean {
        if (s.length !== t.length) return false;

        let alphabetArr: number[] = new Array(26).fill(0);

        for (let i = 0; i < s.length; i++) {
            alphabetArr[s.charCodeAt(i) - 97]++;
            alphabetArr[t.charCodeAt(i) - 97]--;
        }

        return alphabetArr.every((char) => char === 0);
    }

    return arrayFunc(s, t);
}
