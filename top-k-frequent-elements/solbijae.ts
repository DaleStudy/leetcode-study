function topKFrequent(nums: number[], k: number): number[] {
    const map = new Map();

    for (let i=0; i<nums.length; i++) {
        const num = nums[i]
        map.set(num, (map.get(num)|| 0) + 1 );
    }

    return [...map.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, k)
        .map(([key]) => key);
};

// 시간 복잡도: O(n log n)
// 공간 복잡도: O(n)
