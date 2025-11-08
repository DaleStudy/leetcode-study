function topKFrequent(nums: number[], k: number): number[] {
    const dict = nums.reduce((acc: Record<number, number>, v) => {
        if(acc[v] != null) {
            acc[v] += 1;
        } else {
            acc[v] = 1
        }
        return acc;
    }, {});
    
  
    const result = Object.entries(dict).sort((a, b) => b[1] - a[1]).slice(0, k);
    return result.map(([key]) => parseInt(key));
};