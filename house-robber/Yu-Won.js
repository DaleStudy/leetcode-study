/**
 * 문제: https://leetcode.com/problems/house-robber/description/
 *
 * 요구사항:
 * nums: number[]를 Input 으로 받았을 때
 * 인접하지 않은 데이터들의 합 중 가장 큰 값을 리턴한다.
 *
 * * */

const houseRobber = (nums) => {
    let prev1 = 0;
    let prev2 = 0;
    for(let i = 0; i < nums.length; i++) {
        let current = Math.max(nums[i] + prev2, prev1);
        prev2 = prev1;
        prev1 = current;
    }
    return prev1;
}
