/**
 * [Problem]: [125] Valid Palindrome
 *
 * (https://leetcode.com/problems/valid-palindrome/description/)
 */

function isPalindrome(s: string): boolean {
    // 시간복잡도: O(n)
    // 공간복잡도: O(n)
    function twoPointerFunc(s: string): boolean {
        let stringArr: string[] = [...s.replace(/[^a-zA-Z0-9]/g, "")];
        let left = 0;
        let right = stringArr.length - 1;

        while (left < right) {
            if (stringArr[left].toLowerCase() === stringArr[right].toLowerCase()) {
                left++;
                right--;
            } else {
                return false;
            }
        }

        return true;
    }

    // 시간복잡도: O(n)
    // 공간복잡도: O(1)
    function optimizedTwoPointerFunc(s: string): boolean {
        let left = 0;
        let right = s.length - 1;

        while (left < right) {
            while (left < right && !isLetterOrDigit(s[left])) left++;
            while (left < right && !isLetterOrDigit(s[right])) right--;

            if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;
            left++;
            right--;
        }

        return true;

        function isLetterOrDigit(c: string): boolean {
            return /[a-zA-Z0-9]/.test(c);
        }
    }
    return optimizedTwoPointerFunc(s);
}
