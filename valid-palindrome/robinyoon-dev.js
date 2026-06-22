/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {

    //NOTE: 다음에는 투 포인터 방식으로 불어보겠습니다...

    //0. 엣지케이스 대비: 빈칸인 경우.
    if (s.trim() === '') {
        return true;
    }

    //1. s를 array로 변환
    const sArray = Array.from(s);

    // 알파벳만 남기는 작업 
    // (Alphanumeric characters include letters and numbers.)
    const aAscii = 'a'.charCodeAt(0);
    const zAscii = 'z'.charCodeAt(0);
    const aUpperAscii = 'A'.charCodeAt(0);
    const zUpperAscii = 'Z'.charCodeAt(0);
    const zeroAscii = '0'.charCodeAt(0);
    const nineAscii = '9'.charCodeAt(0);

    const filteredArray = [];
    for (let char of sArray) {
        let charAscii = char.charCodeAt(0);

        let isCharacter = (charAscii >= aAscii && charAscii <= zAscii) || (charAscii >= aUpperAscii && charAscii <= zUpperAscii) || (charAscii >= zeroAscii && charAscii <= nineAscii);

        if (isCharacter) {
            filteredArray.push(char);
        }
    }

    // 대문자 -> 소문자로 변경하는 작업
    const lowerArray = [];
    for (let char of filteredArray) {
        lowerArray.push(char.toLowerCase());
    }

    // reverse 해도 똑같은지 확인하는 작업
    const reversedArray = [...lowerArray].reverse();

    const originalString = lowerArray.join();
    const reversedString = reversedArray.join();

    return originalString === reversedString;

};

