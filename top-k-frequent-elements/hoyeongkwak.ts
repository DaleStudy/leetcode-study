////////////
/*
시간복잡도 : O(n + m log m)
공간복잡도 : O(m)
*/
function topKFrequent(nums: number[], k: number): number[] {
    const numMap = new Map<number, number>()
    for(const num of nums) {
        if (!numMap.has(num)) {
            numMap.set(num, 1)
        } else {
            const numCnt = numMap.get(num)
            numMap.set(num, numCnt + 1)
        }
    }
    const numArray = Array.from(numMap).sort((a, b) => b[1] - a[1])
    const result = []
    for(let idx = 0; idx < k; idx++){
        result.push(numArray[idx][0])
    }
    return result
};