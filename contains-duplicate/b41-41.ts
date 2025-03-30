// nums에 중복이 있는 지 확인하는 것
// array써서 시간 통과 못했다가 Set 객체로 변경해서 통과
function containsDuplicate(nums: number[]): boolean {
    const numSet = new Set();

    for(let num of nums) {
        if(numSet.has(num)) {
            return true;
        } else {
            numSet.add(num);
        }
    }

    return false;
};