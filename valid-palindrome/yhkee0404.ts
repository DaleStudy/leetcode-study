function isPalindrome(s: string): boolean {
    const isAlpha = x => x.toLowerCase() >= 'a' && x.toLowerCase() <= 'z';
    const isNumeric = x => x >= '0' && x <= '9';
    const isAlphanumeric = x => isAlpha(x) || isNumeric(x);
    let i = 0, j = s.length - 1;
    while (i < j) {
        while (i !== j && ! isAlphanumeric(s[i])) {
            i++;
        }
        while (i !== j && ! isAlphanumeric(s[j])) {
            j--;
        }
        if (s[i].toLowerCase() !== s[j].toLowerCase()) {
            return false;
        }
        i++, j--;
    }
    return true;
};
