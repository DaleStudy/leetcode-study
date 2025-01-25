/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
    const binary = [1];

    while (binary[0] < n) {
        const latest = binary[0] * 2;

        binary.unshift(latest);
    }

    let count = 0;

    for (let i = 0; i < binary.length; i++) {
        if (binary[i] <= n) {
            count++;
            n = n - binary[i];
        }

        if (n === 0) {
            break;
        }
    }

    return count;
};

// 시간복잡도 O(logn) -> 이진탐색처럼 2씩 곱해가며 n을 넘어가는 가장 큰 수를 찾으므로
