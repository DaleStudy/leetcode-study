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

    // 배열로 변경
    let entries = Object.entries(obj)
    // 정렬
    let sort_arr = entries.sort((a, b) => Number(b[1]) - Number(a[1]));

    let result = [];
    let l = 0;
    for(const item of sort_arr) {
        if(l == k) break;
        result.push(Number(item[0]));
        l++;
    }

    return result;
};
