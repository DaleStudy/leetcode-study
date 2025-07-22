function twoSum(nums: number[], target: number): number[] {
    let answer = []
    for(let i = 0 ; i < nums.length; i ++){
        let temp = target - nums[i]
        if (nums.includes(temp) && temp != nums[i]) {
            const index = nums.findIndex((test) => test === temp )
            answer.push(index)
}
    }
return answer 
};