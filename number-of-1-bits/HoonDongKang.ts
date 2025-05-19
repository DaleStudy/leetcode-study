/**
 * [Problem]: [191] Number of 1 Bits
 *
 * (https://leetcode.com/problems/number-of-1-bits/description/)
 */
function hammingWeight(n: number): number {
    // 시간 복잡도 O(log n)
    // 공간 복잡도 O(1)
    function divisionFunc(n: number): number {
        let count = 0;
        while (n > 0) {
            count += n % 2;
            n = Math.floor(n / 2);
        }

        return count;
    }

    // 시간 복잡도 O(log n)
    // 공간 복잡도 O(1)
    function bitwiseFunc(n: number): number {
        let count = 0;
        while (n !== 0) {
            count += n & 1;
            n = n >>> 1;
        }

        return count;
    }
    return divisionFunc(n);
}
