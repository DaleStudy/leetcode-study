function rob(nums: number[]): number {
    // 첫시도: 아예 떨어져있는 경우를 고려하지 않음 (통과 안됨)
    // let evenSum = 0;
    // let oddSum = 0;
    
    // for (let i=0; i<nums.length; i++) {
    //     if (i % 2 === 0) {
    //         evenSum += nums[i];
    //     } else {
    //         oddSum += nums[i];
    //     }
    // }

    // return Math.max(evenSum, oddSum);

    // 시간복잡도 O(n), 공간복잡도 O(1)
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0];

    let prev = nums[0];
    let max = Math.max(nums[0], nums[1]);

    for (let i = 2; i < nums.length; i++) {
        const current = Math.max(max, prev + nums[i]);
        prev = max;
        max = current;
    }

    return max;
};
