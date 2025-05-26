/**
 * [Problem]: [647] Palindromic Substrings
 * (https://leetcode.com/problems/palindromic-substrings/description/)
 */

function countSubstrings(s: string): number {
    //시간복잡도 O(n^3)
    //공간복잡도 O(1)
    function bruteForceFunc(s: string): number {
        let count = 0;

        for (let i = 0; i < s.length; i++) {
            for (let j = i; j < s.length; j++) {
                if (isPanlindrome(i, j)) count++;
            }
        }

        function isPanlindrome(left: number, right: number): boolean {
            while (left < right) {
                if (s[left] !== s[right]) return false;
                left++;
                right--;
            }

            return true;
        }

        return count;
    }
    //시간복잡도 O(n^2)
    //공간복잡도 O(n^2)
    function dpFunc(s: string): number {
        const dp = new Map<string, boolean>();
        let count = 0;

        for (let end = 0; end < s.length; end++) {
            for (let start = end; start >= 0; start--) {
                const key = `${start},${end}`;
                if (start === end) {
                    dp.set(key, true);
                } else if (start + 1 === end) {
                    dp.set(key, s[start] === s[end]);
                } else {
                    const innerKey = `${start + 1},${end - 1}`;
                    const isInnerPalindrome = dp.get(innerKey) || false;
                    dp.set(key, s[start] === s[end] && isInnerPalindrome);
                }

                if (dp.get(key)) {
                    count++;
                }
            }
        }

        return count;
    }
}
