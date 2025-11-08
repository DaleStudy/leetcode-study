function containsDuplicate(nums: number[]): boolean {
    const set = new Set();
    for(const num of nums) {
        if(set.has(num)) {
            return true;
        }
        set.add(num);
    }

    return false;
};