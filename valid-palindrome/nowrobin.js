/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // 1. 소문자로 변환 + 알파벳/숫자만 남기기
    // (공백, 특수문자 제거)
    s = s.toLowerCase().replace(/[^a-z0-9]/g, "");

    const length = s.length;

    // 2. 문자열의 절반만 순회하면서 양쪽 비교
    for (let i = 0; i < length / 2; i++) {
        // 왼쪽(i) vs 오른쪽(length - 1 - i)
        if (s[i] !== s[length - 1 - i]) {
            // 하나라도 다르면 팰린드롬 아님
            return false;
        }
    }

    // 3. 끝까지 문제 없으면 팰린드롬
    return true;
};
