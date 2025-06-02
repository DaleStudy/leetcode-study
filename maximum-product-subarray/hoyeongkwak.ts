/*
Time complexity : O(n)
Space complexity : O(1)
*/
function maxProduct(nums: number[]): number {
    let max = 1
    let min = 1
    let result = nums[0]
    nums.forEach((num) => {
        const tempMax = Math.max(num, max * num, min * num)
        min = Math.min(num, max * num, min * num)
        max = tempMax
        result = Math.max(result, max)
    })
    return result
}
