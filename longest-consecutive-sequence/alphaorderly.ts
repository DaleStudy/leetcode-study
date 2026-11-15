// 시간복잡도 : O(n)
// 공간복잡도 : O(n)
function longestConsecutive(nums: number[]): number {
    const numbers = new Set(nums);
    let ans = 0;

    for (const num of numbers) {
        if (numbers.has(num - 1)) continue;

        let current = num;
        let count = 0;

        while (numbers.has(current)) {
            count += 1;
            current += 1;
        }

        ans = ans > count ? ans : count;
    }

    return ans;
};
