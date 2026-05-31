/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
    let count = 0;
    let tempN = n;
    while (tempN != 0) {
        if (tempN & 1) {
            // 비트 마스크(& 1): 앞의 비트들은 모두 0으로 무시하고, 맨 끝자리 비트만 추출하여 검사.
            count++;
        }
        tempN = tempN >>> 1;
        // >>: 부호 유지 우측 이동
        // >>>: 부호 상관없이 0으로 채우는 우측 이동
    }

    return count;
};
