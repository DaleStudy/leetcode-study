function longestConsecutive(nums: number[]): number {
    // 첫 시도: sort때문에 시간 복잡도가 O(n log n)라 O(n)에 풀어야 한다는 요구사항 만족하지 못함, 공간복잡도는 O(n)
    // if (nums.length === 0) return 0;
    // const sorted = [...new Set(nums)].sort((a, b) => a-b);
    // let max = 1;
    // let current = 1;

    // for (let i=0; i<nums.length; i++) {
    // console.log(sorted[i])
    // if (sorted[i+1] - sorted[i] === 1) {
    //     current += 1;
    // } else {
    //     current = 1;
    // }

    // max = Math.max(max, current);
    // }

    // return max;

    // 두번째 시도: 시간, 공간복잡도 O(n)
    if (nums.length === 0) return 0;
    
    const numSet = new Set(nums);
    let current = 0;
    let consecutive = 1;
    let max = 1;

    for (let num of numSet) {
        if (!numSet.has(num - 1)) {
            current = num;
            consecutive = 1;

            while (numSet.has(current + 1)) {
                consecutive += 1;
                current = current + 1;
            }

            max = Math.max(consecutive, max);
        }
    }

    return max;
};
