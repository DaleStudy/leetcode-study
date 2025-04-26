/**
 * 주어진 숫자를 2진수로 표현했을 때 비트가 1인 개수를 반환하는 함수
 * @param {number} n
 * @return {number}
 */
const hammingWeight = function(n) {
    const binary = n.toString(2);
    return Array.from(binary).filter((bit) => bit == 1).length;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
