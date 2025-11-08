function topKFrequent(nums: number[], k: number): number[] {
    // nums 순회하면서 각 숫자 개수 카운트
    const dict = nums.reduce((acc: Record<number, number>, v) => {
        if(acc[v] != null) {
            acc[v] += 1;
        } else {
            acc[v] = 1
        }
        return acc;
    }, {});
    
  
    // 내림차순으로 정렬하고, k개 만큼 자르고 배열로 반환
    const result = Object.entries(dict).sort((a, b) => b[1] - a[1]).slice(0, k);
    return result.map(([key]) => parseInt(key));
};
