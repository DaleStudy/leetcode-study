// NOTE: set을 사용해서 중복된 엘리먼트가 있는 경우 true 리턴
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