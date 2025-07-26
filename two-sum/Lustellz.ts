function twoSum(nums: number[], target: number){
    for(let i = 0; i < nums.length; i++){
        for(let j = i+1; nums.length-j;j++)
        if(nums[j] === target - nums[i]) return [i, j]
    }
};
