function combinationSum(candidates: number[], target: number, dp = new Map()): number[][] {
    if (target <= 0) {
        return [];
    }
    let ans = dp.get(target);
    if (ans !== undefined) {
        return ans;
    }
    ans = [];
    for (const candidate of candidates) {
        if (target == candidate) {
            ans.push([candidate]);
            continue;
        }
        for (const combination of combinationSum(candidates, target - candidate, dp)) {
            if (combination[combination.length - 1] > candidate) {
                continue;
            }
            ans.push([...combination, candidate]);
        }
    }
    dp.set(target, ans);
    return ans;
};
