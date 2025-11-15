function longestConsecutive(nums: number[]): number {
    const set = new Set(nums);
    let maxCount = 0;

    for (const num of set) {
        // 시작 시점이 되는 숫자부터 시작.
        const isStart = !set.has(num - 1);
        if(!isStart) continue;

        let count = 0;
        let _num = num;
        while(true) {
            count += 1;
            const hasNext = set.has(_num + 1);

            // 다음 요소가 없을 때 까지 순회하다가 최대 카운트를 override
            if(!hasNext) {
                maxCount = Math.max(maxCount, count);
                break;
            }

            // 한 번 사용한 숫자는 제거
            set.delete(_num);
            _num+=1;
        } 
    }

    return maxCount
};
