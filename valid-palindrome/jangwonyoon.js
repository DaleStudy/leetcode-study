/**
 * @param {string} s
 * @return {boolean}
 */

/**
 * 문자열 다루기 문제
 * 문자열을 처리하는 시간은 문자열의 길이에 비례하므로 O(n)이다.
 * 문자열을 뒤집기 위해 새로운 문자열을 생성하는 시간은 문자열의 길이에 비례하므로 O(n)이다.
 *
 * 시간 복잡도: O(n) - 문자열을 처리하는 시간
 * 공간 복잡도: O(n) - 문자열을 뒤집기 위해 새로운 문자열을 생성
 *
 *
 * 1. 소문자로 바꾸고, 알파벳과 숫자만 남김 (공백, 특수문자 제거)
 * 2. 문자열을 뒤집기
 * 3. 뒤집은 문자열과 원래 문자열이 같은지 비교
 * 4. 같으면 true, 다르면 false 반환
 */

var isPalindrome = function(s) {
    // 소문자로 바꾸고, 알파벳과 숫자만 남김 (공백, 특수문자 제거)
    const cleanedStr = s.toLowerCase().replace(/[^a-z0-9]/g, '');

    // 문자열을 뒤집기
    const reversedStr = cleanedStr.split("").reverse().join("");

    return cleanedStr === reversedStr;
}
