const isAlphaNumeric = (ch: string) => (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9')

function isPalindrome(s: string): boolean {
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        while (left < s.length && !isAlphaNumeric(s[left])) {
            left += 1
        }

        while (right >= 0 && !isAlphaNumeric(s[right])) {
            right -= 1
        }

        if (left >= right) break;

        if (s[left].toLowerCase() != s[right].toLowerCase()) return false;

        left += 1
        right -= 1
    }

    return true
};
