/**
 * https://leetcode.com/problems/valid-anagram/
 * time complexity : O(n)
 * space complexity : O(n)
 */

function isAnagram(s: string, t: string): boolean {
    const count: Record<string, number> = {};
    if (s.length !== t.length) return false;

    for (let char of s) {
        if (count[char] === undefined) {
            count[char] = 1;
        } else {
            count[char] += 1;
        }
    }
    
    for (let char of t) {
        if (!count[char]) {
            return false;
        } else {
            count[char] -= 1;
        }
    }
    
    return Object.values(count).every(v => v === 0);
};
