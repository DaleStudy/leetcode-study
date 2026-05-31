/**
 * 문제: https://leetcode.com/problems/3sum/description/
 *
 * 요구사항:
 * nums: number[]가 주어질 때 3개의 합이 0이되는 배열을 리턴한다.
 *
 * * */

const threeSum = (nums) => {
    let result = [];

    nums.sort((a,b) => a-b);

    for(let i = 0; i <nums.length-2; i++) {
        if(i > 0 && nums[i] === nums[i-1]) continue;

        if(nums[i] > 0) break;

        let left= i+1;
        let right = nums.length -1;

        while(left < right) {
            let sum = nums[i] + nums[left] + nums[right];

            if(sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);

                while(left < right && nums[left] === nums[left+1]) left++;
                while(left < right && nums[right] === nums[right-1]) right++;
                left++;
                right--;
            } else if (sum <0) {
                left++;
            } else {
                right--;
            }
        }
    }
    return result;
}
