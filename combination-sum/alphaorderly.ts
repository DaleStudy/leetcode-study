function combinationSum(candidates: number[], target: number): number[][] {
    const ans: number[][] = [];
    const app: number[] = [];

    backtracking(candidates, 0, target, ans, app);

    return ans;
};

function backtracking(nums: number[], index: number, target: number, ans: number[][], app: number[]): void {
    if (target == 0) {
        ans.push([...app]);
        return;
    }

    for (let i = index; i < nums.length;i += 1) {
        if (target - nums[i] < 0) continue;

        app.push(nums[i])
        backtracking(nums, i, target - nums[i], ans, app)
        app.pop()
    }
}
