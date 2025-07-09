/**
 * [Problem]: [5] Longest Palindromic Substring
 * (https://leetcode.com/problems/longest-palindromic-substring/)
 */
// 시간복잡도 O(n^2)
// 공간복잡도 O(1)
function longestPalindrome(s: string): string {
    if (s.length < 2) return s;

    let start = 0;
    let end = 0;

    function findPalindrome(left: number, right: number): void {
        while (0 <= left && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }

        if (right - left - 1 > end - start) {
            start = left + 1;
            end = right - 1;
        }
    }

    for (let i = 0; i < s.length; i++) {
        findPalindrome(i, i);
        findPalindrome(i, i + 1);
    }

    return s.substring(start, end + 1);
}
