/**
 * https://leetcode.com/problems/longest-consecutive-sequence
 * time complexity : O(n)
 * space complexity : O(n)
 */
const findStreak = (set: Set<number>) => (num: number): number => {
    if (!set.has(num - 1)) return takeWhile(num, currentNum => set.has(currentNum)).length;
    return 0;
};

const takeWhile = (start: number, predicate: (value: number) => boolean): number[] => {
    const result: number[] = [];
    let currentNum = start;
    while (predicate(currentNum)) {
        result.push(currentNum);
        currentNum += 1;
    }
    return result;
}

const max = (maxStreak: number, currentStreak: number): number => Math.max(maxStreak, currentStreak);

function longestConsecutive(nums: number[]): number {
    const numSet = new Set(nums);

    return [...numSet]
        .map(findStreak(numSet))
        .reduce(max, 0);
}
