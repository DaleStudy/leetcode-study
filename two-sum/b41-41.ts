// 1차 시도
// function twoSum(nums: number[], target: number): number[] {
//     for(const index in nums) {
//         for(const index2 in nums) {
//             if (index !== index2) {
//                 if(target === nums[index] + nums[index2]) {
//                     return [Number(index), Number(index2)]  
//                 }
//             }
//         }
//     }
// };

// 2차 시도
function twoSum(nums: number[], target: number): number[] {
    for (const index in nums) {
        for (let index2 = Number(index) + 1; index2 < nums.length; index2++) {
            if(target === nums[index] + nums[index2]) {
                return [Number(index), Number(index2)]
            }
        }
         
    }

	return [];
};
