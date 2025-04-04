function topKFrequent(nums: number[], k: number): number[] {
    const numMap = new Map();

    for (let num of nums) {
        if(!numMap.has(num)) {
            numMap.set(num, 1);
        } else {
            const count = Number(numMap.get(num)) || 0;
            numMap.set(num, count + 1);
        }
    }

    const result = [...numMap].sort((a, b) => b[1] - a[1]).map((num) => num[0]).slice(0, k);
    

    return result;
};
