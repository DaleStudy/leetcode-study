/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a,b) => a-b);
    const length = nums.length;

    const answer = [];
    

    for(let i = 0; i < length - 2; i++){
        if(i > 0 && nums[i] === nums[i-1]) continue;
        if(nums[i] > 0) break;

        let left = i + 1;
        let right = length -1;
        
        while(left < right){
            const result = nums[left]+ nums[right] + nums[i];
            
            if(result > 0) {
                right -= 1;
            }

            if(result < 0) {
                left +=1;
            }

            if(result === 0) {
                answer.push([nums[i],nums[left],nums[right]]);

                while(left < right && nums[left] === nums[left + 1]) left += 1;
                while(left < right && nums[right] === nums[right - 1]) right -=1;

                left += 1;
                right -= 1;
            }
        }

        
    }

    return answer    
};
