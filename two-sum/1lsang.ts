// 1. 가장 간단한 방법 이중 for문 (Runtime: 175ms / Memory: 55.8MB)
// function twoSum(nums: number[], target: number): number[] {
//     const length = nums.length;
//     for (let i = 0; i < length; i++) {
//         for (let j = 0; j < length; j++) {
//             if (i === j) continue;
//             if (nums[i] + nums[j] === target) return [i, j]
//         }
//     }
//     return [];
// };

// 2. 시간 복잡도 개선 (Runtime: 9ms / Memory: 60.4MB)
function twoSum(nums: number[], target: number): number[] {
    const numObj = {};
    nums.forEach((num, index) => {numObj[num] ? numObj[num].push(index) : numObj[num]=[index]});
    for (let i = 0; i<nums.length; i++) {
        const num = target - nums[i];
        if (numObj[num]?.length === 1) {
            if (i === numObj[num][0]) continue;
            return [i, numObj[num][0]];
        }
        else if (numObj[num]?.length === 2) {
            return numObj[num];
        }
    }
    return [];
};
