
// 시간복잡도 : O(n)
// 공간복잡도 : O(n)
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map<number, number>();

    for (const num of nums) {
        freq.set(num, (freq.get(num) ?? 0) + 1);
    }

    const buckets: number[][] = Array.from(
        { length: nums.length + 1 },
        () => []
    );

    for (const [num, count] of freq) {
        buckets[count].push(num);
    }

    const result: number[] = [];

    for (let i = buckets.length - 1; i >= 0; i--) {
        for (const num of buckets[i]) {
            result.push(num);

            if (result.length === k) {
                return result;
            }
        }
    }

    return result;
}
