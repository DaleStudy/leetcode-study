/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    // 0이 2개 이상인 경우에는 무조건 0
    if(nums.filter((num) => num === 0).length > 1) return Array.from({length:nums.length}).fill(0);

    // 0이  1개인 경우에 나타나는 수
    const hasZero = nums.includes(0);

    const allMatrix = nums.filter(Boolean). reduce((acc, cur) => (acc * cur),1);

    return nums.map((num) => {
        if(hasZero){
            if(num !== 0) return 0;

            return allMatrix
        }
    
        return allMatrix / num
    });
};
