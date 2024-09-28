/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * time complexity : O(n)
 * space complexity : O(n)
 */
function lengthOfLongestSubstring(s: string): number {
    let n = s.length, ans = 0;
    const map = new Map<string, number>();
    for (let j = 0, i = 0; j < n; j++) {
        if (map.has(s[j])) {
            i = Math.max((map.get(s[j]) ?? 0) + 1, i);
        }
        ans = Math.max(ans, j - i + 1);
        map.set(s[j], j);
    }
    return ans;
};
