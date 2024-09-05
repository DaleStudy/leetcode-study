// 시간복잡도 O(n log n)
// 공간복잡도 O(n)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {


    const numsArr = nums.map((num,idx) => [num,idx])
    numsArr.sort((a,b) => a[0] - b[0])


    let leftIdx = 0;
    let rightIdx = nums.length - 1;

    while (leftIdx <= rightIdx) {
        if (numsArr[leftIdx][0] + numsArr[rightIdx][0] === target) {
            return [numsArr[leftIdx][1], numsArr[rightIdx][1]]
        }

        if (numsArr[rightIdx][0] + numsArr[leftIdx][0] > target) {
            rightIdx--
        } else {
            leftIdx++
        }
    }
    return []
};


const nums = [2,7,11,15]
const target = 9

console.log(twoSum(nums,target))
console.log(twoSum([3,2,4],6))
console.log(twoSum([3,3],6))
