function longestConsecutive(nums: number[]): number {
    const sortedNums = [...new Set(nums.sort((a, b) => a - b))];
    const numSet = new Set();

    let dummy: number[] = [];

    for (let i: number = 0; i < sortedNums.length; i++) {
        const isConsecutiveSequence = sortedNums[i + 1] - sortedNums[i] === 1;
        const num = sortedNums[i];

        if(!isConsecutiveSequence) {
            dummy.push(num)
            numSet.add(dummy.length);
            dummy = [];
        } else {
            dummy.push(num);
        }
    }
    
    numSet.add(dummy.length);
    
    const result = [...numSet].sort((a, b) => Number(b) - Number(a)) as number[];
    return result[0] || 0;
}
