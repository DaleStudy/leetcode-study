/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const lowercase = s.toLowerCase(); // 소문자로 변환
    const replacedString = lowercase.replaceAll(/[^a-z0-9]/g,''); // 정규표현식을 통해 영어/숫자가 아닌 값들을 ''로 변환

    
    return replacedString === [...replacedString].reverse().join('') // 기존 문자열과 그 값을 뒤집은 문자열이 같은지 비교
};
