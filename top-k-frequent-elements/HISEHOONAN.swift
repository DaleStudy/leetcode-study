//
//  Top_K_Frequent_Elements .swift
//  Algorithm
//
//  Created by 안세훈 on 3/31/25.
//

class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var dic : [Int : Int] = [:]

        for i in nums {
            dic[i] = dic[i , default : 0] + 1
        }

        var sortarray = dic.sorted{$0.value > $1.value}
        var answer : [Int] = []

        for i in 0..<k{
            answer.append(sortarray[i].key)
        }
        print(sortarray)
        print(answer)
        return answer
    }
}
