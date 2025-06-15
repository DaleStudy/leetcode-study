/**
 * [Problem]: [268] Missing Number
 * (https://leetcode.com/problems/missing-number/description/)
 */
function missingNumber(nums: number[]): number {
    //시간복잡도 O(n^2)
    //공간복잡도 O(1)
    function loopFunc(nums: number[]): number {
        let num = 0;
        while (true) {
            if (!nums.includes(num)) break;
            num++;
        }

        return num;
    }
    //시간복잡도 O(n)
    //공간복잡도 O(1)
    function sumFunc(nums: number[]): number {
        const n = nums.length;
        const sum = nums.reduce((acc, cur) => (acc += cur), 0);
        const expected = (n * (n + 1)) / 2;

        return expected - sum;
    }
}
