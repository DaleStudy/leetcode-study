/**
 * 주어진 32비트 unsingned integer를 뒤집어 십진수로 반환하는 함수
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
const reverseBits = function(n) {
    const binary = n.toString(2).padStart(32, '0');
    const reversed = Array.from(binary).reverse().join('');
    const decimal = parseInt(reversed, 2).toString(10);

    return Number(decimal);
};

// 시간복잡도: O(1)
// 공간복잡도: O(1)
