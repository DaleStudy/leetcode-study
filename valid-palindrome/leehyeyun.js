/**
 * @param {string} s
 * @return {boolean}
 */
/*
    문자열이 주어졌을 때,
    이 문자열이 '유효한 회문(palindrome)'인지 판별하는 함수.

    회문 판별 규칙:
      - 대문자는 소문자로 변환한다.
      - 영문자(a~z)와 숫자(0~9)만 남기고 나머지 문자는 제거한다.
      - 정제된 문자열을 앞에서 읽은 것과 뒤에서 읽은 것이 같으면 회문이다.

    요청 형식 : isPalindrome(s)

    입력 형식 :
      - s는 문자열(String)
      - 1 <= s.length <= 2 * 10^5
      - 문자열은 ASCII 출력 문자로만 구성됨

    출력 형식 :
      - 유효한 회문이면 true
      - 아니면 false

    예시 :

      Example 1
      입력 :
        s = "A man, a plan, a canal: Panama"
      출력 :
        true
      설명 :
        정제하면 "amanaplanacanalpanama"
        회문이므로 true

      Example 2
      입력 :
        s = "race a car"
      출력 :
        false
      설명 :
        정제하면 "raceacar"
        회문이 아님

      Example 3
      입력 :
        s = " "
      출력 :
        true
      설명 :
        정제 후 "" (빈 문자열)
        빈 문자열은 회문으로 간주됨

    제약사항 :
      - 문자열의 길이가 매우 크므로 O(n) 방식이 적합함
*/
var isPalindrome = function(s) {

    let cleanString = s.toLowerCase().replace(/[^a-z0-9]/g, '');

    let splitString = cleanString.split("");
    let reverseArray = splitString.reverse();
    let joinArray = reverseArray.join("");

    if(cleanString != joinArray)
    {
        return false
    }else {
        return true
    }
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("race a car"));
console.log(isPalindrome(" "));

