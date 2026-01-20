function missingNumber(nums: number[]): number {
    let occurence = new Map<number, boolean>();

    for (let i = 0; i <= nums.length; i++) {
        occurence.set(i, false);
    }

    for (const num of nums) {
        occurence.set(num, true);
    }

    const results = Array.from(occurence.entries());

    for (const result of results) {
        if (result[1] === false) {
            return result[0];
        }
    }

    return 0;
};
