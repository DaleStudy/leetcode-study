/**
 * https://leetcode.com/problems/palindromic-substrings/
 * time complexity : O(n^2)
 * space complexity : O(n)
 */

const expandAroundCenter = (s: string, left: number, right: number): number => {
    if (left < 0 || right >= s.length || s[left] !== s[right]) {
        return 0;
    }
    return 1 + expandAroundCenter(s, left - 1, right + 1);
};

function countSubstrings(s: string): number {

    return [...Array(s.length).keys()].reduce((totalCount, i) => {
        return totalCount +
            expandAroundCenter(s, i, i) +
            expandAroundCenter(s, i, i + 1);
    }, 0);
};
