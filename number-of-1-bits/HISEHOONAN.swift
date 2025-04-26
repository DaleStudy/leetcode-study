//
//  Untitled.swift
//  Algorithm
//
//  Created by 안세훈 on 4/14/25.
//

class Solution {
    func hammingWeight(_ n: Int) -> Int {
        var num = n //n을 저장할 변수
        var remain = 0 //나머지를 저장할 변수
        var array : [Int] = [] //이진법으로 변환한 수를 저장할 배열

        while num > 0{ //num이 0보다 클때만 반복
            remain = num % 2 //num을 2로 나눈 나머지를 저장
            num = num / 2 //num을 2로 나눈 몫을 저장
            array.append(remain) //array에 나머지를 저장
        }
        
        return array.filter{$0 == 1}.count //array에 1만 추출한 후 그 개수 리턴
    }
}
