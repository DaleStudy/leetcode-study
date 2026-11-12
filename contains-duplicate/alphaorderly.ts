// 시간복잡도 : O(n)
// 공간복잡도 : O(n)
function containsDuplicate(nums: number[]): boolean {
    const list = new Set<number>();

    for (const num of nums) {
        if (list.has(num)) {
            return true;
        }
        list.add(num);
    }

    return false;
};
