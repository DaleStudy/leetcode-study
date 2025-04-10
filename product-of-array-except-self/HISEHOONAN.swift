//
//  239.swift
//  Algorithm
//
//  Created by 안세훈 on 4/8/25.
//

//Product of Array Except Self 
class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {

        var array1 : [Int] = nums            // 원래 배열
        var array2 : [Int] = nums.reversed() // 뒤집은 배열

        var array1Forloop : [Int] = []       // 원래 배열을 계산 후 저장할 배열
        var array2Forloop : [Int] = []       // 뒤집은 배열을 계산 후 저장할 배열

        var multiply = 1                     // 연산용

        var result : [Int] = []              // 최종 결과를 담을 배열

        // 원래 누적 곱 계산 (자기 자신 제외)
        for num in array1 {
            array1Forloop.append(multiply)  // 현재까지의 누적 곱을 저장 (시작은1)
            multiply = num * multiply       // 누적 곱 업데이트
        }

        multiply = 1                        //뒤집은 배열 계산을 위해 초기화

        // 뒤집은 배열 누적 곱 계산 (자기 자신 제외)
        for num in array2 {
            array2Forloop.append(multiply)  // 현재까지의 누적 곱을 저장
            multiply = num * multiply       // 누적 곱 업데이트
        }

        array2Forloop = array2Forloop.reversed()// 뒤집은 배열 곱을 원래 순서로 되돌림

        // 원래 배열 곱과 뒤집은 배열 곱의 인덱스가 같은놈들끼리
        // 곱해서 최종 결과 생성
        for i in 0..<nums.count {
            result.append(array1Forloop[i] * array2Forloop[i])
        }

        return result
    }
}
