function isPalindrome(s: string): boolean {

    // 풀이 1:
    // lowcase 변환, 졍규식으로 문자 이외 필터
    // 필터된 문자열 순회하면서 (i, length - i)
    // 전부 일치하면 true 아니면 false
    // 시간 복잡도: O(n)
    // 공간 복잡도: O(n)

    const validPalindrome1 = () => {
        const sanitizedStrArr = [...s.toLowerCase().replace(/[^a-z0-9]/g, "")];

        for(let i = 0; i < Math.floor(sanitizedStrArr.length / 2); i++) {
            if(sanitizedStrArr[i] !== sanitizedStrArr[(sanitizedStrArr.length - 1) - i]) {
                return false;
            }
        }

        return true;
    }

    return validPalindrome1();
};
