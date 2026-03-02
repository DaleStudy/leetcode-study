function containsDuplicate(nums: number[]): boolean {
    const uniqueNums = new Set<number>(nums);
    return uniqueNums.size < nums.length
};
