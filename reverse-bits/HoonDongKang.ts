/**
 * [Problem]: [190] Reverse Bits
 * (https://leetcode.com/problems/reverse-bits/description/)
 */
function reverseBits(n: number): number {
    //시간복잡도 O(1)
    //공간복잡도 O(1)
    function stackFunc(n: number): number {
        const stack: number[] = [];
        let output = 0;
        let scale = 1;

        while (stack.length < 32) {
            stack.push(n % 2);
            n = Math.floor(n / 2);
        }

        while (stack.length) {
            output += stack.pop()! * scale;
            scale *= 2;
        }

        return output;
    }
    //시간복잡도 O(1)
    //공간복잡도 O(1)
    function bitFunc(n: number): number {
        let result = 0;
        for (let i = 0; i < 32; i++) {
            result <<= 1;
            result |= n & 1;
            n >>>= 1;
        }

        return result >>> 0;
    }
}
