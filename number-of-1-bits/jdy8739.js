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

// 수정된 시간복잡도 -> 위의 while 문에서 O(logn)의 시간복잡도를 수행하면서 O(n)의 시간복잡도를 갖는 unshift 메소드를 사용하며
// for문에서 다시 O(logn)의 시간복잡도의 루프를 돌기 때문에
// 총 복잡도는 O(logn) * binary 배열의 길이 + O(logn)
