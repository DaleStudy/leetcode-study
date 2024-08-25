/**
 * https://leetcode.com/problems/valid-anagram/submissions
 * time complexity : O(n)
 * space complexity : O(n)
 */
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const map = {};

    for (const char of s) map[char] = (map[char] ?? 0) + 1;

    for (const char of t) {
        if (map[char] !== undefined) {
            map[char] = map[char] - 1;
        } else return false;
    }

    for (const val of Object.values(map)) if (val !== 0) return false;

    return true;
};
