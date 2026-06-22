/**
 * @param {number} n - 32비트 정수
 * @return {number} - 이진수에서 1의 개수
 */
var hammingWeight = function(n) {
    let setBitCount = 0; // 1의 개수를 저장할 변수

    // n이 0이 될 때까지 반복 (모든 1비트를 제거할 때까지)
    while (n !== 0) {
        // 가장 오른쪽에 있는 1비트를 제거
        // 예: 101100 -> 101000
        n &= (n - 1);

        // 1비트 하나 제거했으므로 카운트 증가
        setBitCount++;
    }

    // 총 1의 개수 반환
    return setBitCount;
};

