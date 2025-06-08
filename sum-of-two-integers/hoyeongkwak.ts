/*
Time complexity : O(1)
Space complexity : O(1)
*/
function getSum(a: number, b: number): number {
    let xor = a ^ b
    let carry = (a & b) << 1

    while (carry !== 0) {
        const tempXor = xor ^ carry
        carry = (xor & carry) << 1
        xor = tempXor
    }
    return xor
};
