function isPalindrome(s: string): boolean {
    // 1. 대문자를 모두 소문자로 바꾼다.
    const lower = s.toLowerCase()
    // 2. 문자와 숫자가 아닌 것은 모두 제거한다.
    const cleaned = lower.replace(/[^a-z0-9]/g,"")
    // 3. 정리된 문자열 뒤집는다.
    const reversed = cleaned.split("").reverse().join("")
    // 4. 정리된 문자열과 뒤집은 문자열이 같으면true, 아니면 false
    if(cleaned === reversed) {
        return true
    } else {
        return false
    }
};
