/**
 *
 * @param nums
 * @param k
 */
function topKFrequent(nums: number[], k: number): number[] {
    let obj = {}

    for(const num of nums) {
        if(!obj[num])
            obj[num] = 0
        ++obj[num]
    }

    return Object.entries(obj)
        .sort((a, b) => Number(b[1]) - Number(a[1]))
        .slice(0, k)
        .map(entry => Number(entry[0]));
};
