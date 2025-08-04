//
//  218.swift
//  Algorithm
//
//  Created by 안세훈 on 4/8/25.
//

//Valid Anagram
class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var sortS = s.sorted() //s를 sort하여 sortS에 저장
        var sortT = t.sorted() //t를 sort하여 sortT에 저장
          
        return sortS == sortT ? true : false //sortS와 sortT가 같다면 true 아니면 false
    }
}
