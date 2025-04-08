//
//  House_Robber .swift
//  Algorithm
//
//  Created by 안세훈 on 3/31/25.
//
///https://leetcode.com/problems/house-robber/description/

class Solution {
    //Dynamic Programming
    func rob(_ nums: [Int]) -> Int {

        if nums.count == 1 {return nums[0]} //배열이 1개인 경우
        if nums.count == 2 {return max(nums[0],nums[1])} //배열이 2개인 경우
        
        var dp = [nums[0], max(nums[0],nums[1])]
                //제일 base가 되는 두 값을 찾는게 제일 중요함.
                //nums[0]은 nums[1]보다 무조건 작아야함.
        for i in 2..<nums.count{
            dp.append(max(dp[i-2]+nums[i],dp[i-1]))
            //dp배열의 i-2번째 배열 + nums의 i번째 배열 vs dp의 i-1번째 배열 중 큰걸 append
            //
        }
        
        return dp[dp.count-1]
    }
}
