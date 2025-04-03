//
//  Contains_Duplicate.swift
//  Algorithm
//
//  Created by 안세훈 on 3/31/25.
//

import Foundation

class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        return nums.count != Set(nums).count
        //Set : 중복된 값을 갖지 않음.
        //문제로 주어진 배열의 개수와 중복을 갖지않는 Set연산의 개수의 차이 비교
        //비교 후 다르다면 true 같다면 false
    }
}
