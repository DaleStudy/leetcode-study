/**
 * @param {number} n
 * @return {number}
 */
/*
문제 설명:
주어진 32비트 부호 있는 정수 n의 비트 순서를 뒤집는 문제이다.

n은 항상 32비트 이진수로 취급되며,
가장 오른쪽 비트는 가장 왼쪽으로,
가장 왼쪽 비트는 가장 오른쪽으로 이동한다.
즉, 32개의 비트 전체를 기준으로 순서를 완전히 반전시킨다.

이때 숫자의 크기나 부호가 아니라,
고정된 32비트 이진 표현 자체를 기준으로 처리해야 하며
앞쪽에 있는 0 비트도 반드시 포함된다.

입력:
- n: 32비트 부호 있는 정수
- 0 ≤ n ≤ 2³¹ − 2
- n은 항상 짝수이다.

출력:
- n의 32비트 이진 표현을 뒤집은 값을 정수로 반환한다.

예시 1:
입력:
  n = 43261596
이진 표현:
  00000010100101000001111010011100
비트 순서 반전:
  00111001011110000010100101000000
출력:
  964176192

예시 2:
입력:
  n = 2147483644
이진 표현:
  01111111111111111111111111111100
비트 순서 반전:
  00111111111111111111111111111110
출력:
  1073741822

추가 조건 (Follow up):
- 이 함수가 매우 자주 호출되는 상황을 가정하고,
  성능을 최적화할 수 있는 방법을 고려해야 한다.
*/

var reverseBits = function(n) {

    const binaryString = n.toString(2).padStart(32, "0");
    const splitString = binaryString.toString().split("");
    const reverseArray = splitString.reverse();
    const joinArray = reverseArray.join("");
    const value = parseInt(joinArray, 2);

    return value;

};

console.log(reverseBits(43261596))
console.log(reverseBits(2147483644))

