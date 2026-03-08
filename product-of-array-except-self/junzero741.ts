// TC: O(n)
// SC: O(1) 
function productExceptSelf(nums: number[]): number[] {
    const answer = new Array(nums.length).fill(1);

    let before = 1;
    for(let i = 0; i < nums.length-1; i++) {
        before *= nums[i];
        answer[i+1] *= before;
    }   
    
    before = 1;
    for(let i = nums.length-1; i > 0; i--) {
        before *= nums[i];
        answer[i-1] *= before;
    }

    return answer;  
};
