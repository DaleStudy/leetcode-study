/**
 * +, - 연산자를 사용하지 않고 a, b를 더하는 함수
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
const getSum = function (a, b) {
    while (b !== 0) {
        [a, b] = [a ^ b, (a & b) << 1]
    }

    return a;
};

// 시간복잡도: O(1)
// 공간복잡도: O(1)
