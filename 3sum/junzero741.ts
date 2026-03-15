// TC: O(n^2)
// SC: O(logn)
function threeSum(nums: number[]): number[][] {
    
    nums.sort((a,b) => a-b);
    const result: number[][] = []

    for(let i = 0 ; i < nums.length; i++) {
        let left = i+1;
        let right = nums.length-1;

        while(left < right) {
           if(i > 0 && nums[i] === nums[i-1]) {
                break;
           }

           const sum = nums[i] + nums[left] + nums[right];
           if(sum > 0) {
                right--;
                continue;
           }
           if(sum < 0) {
                left++;
                continue;
           }
           if(sum === 0) {
                const triplet: number[] = [nums[i], nums[left], nums[right]];
                result.push(triplet);

                while(left < right && nums[left] === nums[left+1]) {
                    left++;
                }
                while(left < right && nums[right] === nums[right-1]) {
                    right--;
                }

                left++;
                right--;
           }
        }
        
    }

    return result;
};
