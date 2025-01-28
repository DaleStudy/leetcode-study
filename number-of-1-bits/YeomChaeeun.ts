/**
 * 10진수 n이 2진수일 때 1을 세기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(logn)
 * - 공간 복잡도: O(logn)
 * @param n
 */
function hammingWeight(n: number): number {
    let binary = "";

    while(n > 0) {
        binary = (n % 2) + binary;
        n = Math.floor(n / 2);
    }

    return [...binary].filter(val => val === '1').length
}
