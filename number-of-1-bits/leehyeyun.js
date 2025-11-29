/**
 * @param {number} n
 * @return {number}
 */
/*
양의 정수 n이 주어졌을 때,
이 정수를 2진수(binary)로 변환했을 때
'1'로 설정된 비트(set bit)의 개수를 구하는 함수.

이 값은 ‘해밍 가중치(Hamming Weight)’라고도 부른다.

요청 형식 : hammingWeight(n)

입력 형식 :
  - n은 양의 정수
  - 1 <= n <= 2^31 - 1

출력 형식 :
  - n의 이진 표현에서 '1'의 개수 (정수)

예시 :

  Example 1
  입력 :
    n = 11
  출력 :
    3
  설명 :
    11 → 1011 (2진수)
    1이 총 3개

  Example 2
  입력 :
    n = 128
  출력 :
    1
  설명 :
    128 → 10000000
    1이 하나뿐

  Example 3
  입력 :
    n = 2147483645
  출력 :
    30
  설명 :
    2147483645 → 1111111111111111111111111111101
    1이 총 30개

제약사항 :
  - 매 호출이 빠르게 동작해야 함
  - 팁: 비트를 하나씩 확인하는 반복문 or
        n &= (n - 1) 같은 비트 최적화가 존재함

참고 :
  - 만약 이 함수를 반복 호출해야 한다면,
    사전 계산된 lookup table을 사용하는 방식으로
    추가 최적화할 수 있다.

*/
var hammingWeight = function(n) {

    let binaryString = n.toString(2);
    let value = binaryString.split("").filter(x => x === "1").length;
    
    return value;
};

console.log(hammingWeight(11));
console.log(hammingWeight(128));
console.log(hammingWeight(2147483645));

