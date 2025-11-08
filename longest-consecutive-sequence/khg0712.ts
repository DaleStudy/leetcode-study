function longestConsecutive(nums: number[]): number {
    const set = new Set(nums);
    let maxCount = 0;

    for (const num of set) {
        const isStart = !set.has(num - 1);
        if(!isStart) continue;

        let count = 0;
        let _num = num;
        while(true) {
            count += 1;
            const hasNext = set.has(_num + 1);

            if(!hasNext) {
                if(count > maxCount) maxCount = count;

                break;
            }

            set.delete(_num);
            _num+=1;
        } 
    }

    return maxCount
};
