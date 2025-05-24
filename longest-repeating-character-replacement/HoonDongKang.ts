/**
 * [Problem]: [424] Longest Repeating Character Replacement
 * (https://leetcode.com/problems/longest-repeating-character-replacement/description/)
 */
function characterReplacement(s: string, k: number): number {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    let left = 0;
    let right = 0;
    let result = 0;
    let map = new Map<string, number>();

    while (right < s.length) {
        map.set(s[right], (map.get(s[right]) || 0) + 1);

        const maxFreq = Math.max(...Array.from(map.values()));
        if (right - left + 1 - maxFreq > k) {
            map.set(s[left], map.get(s[left])! - 1);
            left++;
        }

        result = Math.max(result, right - left + 1);
        right++;
    }

    return result;
}
