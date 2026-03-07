// TC: O(N)
// SC: O(1)
function rob(nums: number[]): number {
    if (nums.length === 0) return 0;

    let prevMax: number = 0; 
    let currMax: number = 0;

    for (const amount of nums) {
        const nextMax: number = Math.max(currMax, prevMax + amount);
        
        prevMax = currMax;
        currMax = nextMax;
    }

    return currMax;
}
