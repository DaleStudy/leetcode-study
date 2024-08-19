/**
 * https://leetcode.com/problems/top-k-frequent-elements/
 * time complexity : O(n)
 * space complexity : O(n)
 */
function topKFrequent(nums: number[], k: number): number[] {
    const record = nums.reduce((acc, curr) => {
        acc[curr] = (acc[curr] ?? 0) + 1;
        return acc;
    }, {});

    const array: Array<number[]> = new Array(nums.length);
    for (const num in record) {
        const v = record[num];
        if (!array[v]) {
            array[v] = [];
        }
        array[v].push(Number(num));
    }

    return array.reduce((acc, curr) => [...curr, ...acc], []).slice(0, k);
};
