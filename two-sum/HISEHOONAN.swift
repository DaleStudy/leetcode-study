//
//  Two_Sum.swift
//  Algorithm
//
//  Created by 안세훈 on 3/31/25.
//

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        for i in 0...nums.count-1{
            for j in i+1...nums.count-1{
                if nums[i] + nums[j] == target{
                    return [i,j]
                }
            }
        }
        return []
    }
    //i번째 인덱스의 값과, j번째 인덱스의 값이 target과 같으면 i,j를 리턴
}
