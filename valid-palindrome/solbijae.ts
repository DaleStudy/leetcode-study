function isPalindrome(s: string): boolean {
    // 첫 시도: 시간/공간 복잡도 O(n)
    // const filtered = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    // if (filtered === filtered.split('').reverse().join('')) return true;
    // return false;

    // 두번째 시도: Two Pointer 사용 - 시간 복잡도 O(n), 공간 복잡도 O(1)
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        while (left < right && !isAlphanumeric(s[left])) left++;
        while (left < right && !isAlphanumeric(s[right])) right--;

        if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;

        left++;
        right--;
    }

    return true;

    function isAlphanumeric(c: string): boolean {
        return /^[a-zA-Z0-9]$/.test(c);
    }
};
