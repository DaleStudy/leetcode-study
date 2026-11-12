// 시간복잡도 : O(n)
// 공간복잡도 : O(n)
function containsDuplicate(nums: number[]): boolean {
    const list = new Set<number>();

    for (const number of nums) {
        if (list.has(number)) {
            return true;
        }
        list.add(number);
    }

    return false;
};
