/**
 * https://leetcode.com/problems/valid-palindrome
 * time complexity : O(n)
 * space complexity : O(n)
 */

const clean = (s: string): string => s.toLowerCase().replace(/[^a-z0-9]/g, "");

const reverse = (s: string): string => s.split("").reverse().join("");

function isPalindrome(s: string): boolean {
    const cleaned = clean(s);
    return cleaned === reverse(cleaned);
};
