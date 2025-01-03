/**
 * 주어진 정수를 32비트로 변환하고 반전시켜 그때의 정수를 반환하는 문제.
 * 
 * @param {number} n - 정수 (32비트))
 * @returns {number} - 2진수 변환 및 반전하여 정수 변환.
 * 
 * 내장 메서드를 사용하여 32비트 2진수 변환 후, reverse하여 다시 정수로 변환.
 * 
 * 시간 복잡도: O(32)
 *  - 32비트 정수의 비트를 처리하므로 고정된 상수 시간.
 * 
 * 공간 복잡도: O(32)
 *  - 2진수 문자열을 생성하고 반전된 문자열을 저장하므로 고정된 크기의 추가 메모리가 필요.
 */
function reverseBits(n: number): number {
    // 숫자를 32비트 2진수 문자열로 변환 (앞에 0 채우기)
    const binaryStr = n.toString(2).padStart(32, '0');
    // 2진수 문자열을 뒤집기
    const reversedBinaryStr = binaryStr.split('').reverse().join('');
    // 뒤집힌 2진수 문자열을 다시 숫자로 변환
    return parseInt(reversedBinaryStr, 2);
};
