//
//  Longest_Consecutive_Sequence.swift
//  Algorithm
//
//  Created by 안세훈 on 3/31/25.
//

///https://leetcode.com/problems/longest-consecutive-sequence/


class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        guard nums.count != 0 else { return 0 }

        var sortednums = Array(Set(nums)).sorted() //중복제거 + 오름차순 정렬
        var maxcount = 1 //최대 카운드
        var count = 1 // 연산용 카운트

        for i in 0..<sortednums.count - 1 {
            if sortednums[i] == sortednums[i+1]-1 {
                //i번째 정렬된 리스트 와 i+1번째 리스트의 값 - 1이 같을 경우
                count += 1 //카운트에 1+
                maxcount = max(maxcount, count) //maxcount는 연산과, max중 큰 것
            } else {
                count = 1  //아니면 1로 초기화.
            }
        }

        return maxcount
    }
}
