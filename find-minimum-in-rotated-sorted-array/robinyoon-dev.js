/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    // nums는 rotated 된 array
    // return 값은 이 nums에서 최솟값을 return 해야함.
    const NUMS_LENGTH = nums.length;

    let result = nums[0];

    for(let i = 0; i < NUMS_LENGTH; i++ ){
        let currentIndex = NUMS_LENGTH - i;

        if(nums[currentIndex - 1] > nums[currentIndex]){
            result = nums[currentIndex];
        }else{
            continue;
        }
    }    
    return result;
};
