//
//  Untitled.swift
//  Algorithm
//
//  Created by 안세훈 on 4/14/25.
//

class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var middleArray : [Int] = [] // 연산중인 배열
        var resultArray : [[Int]] = [] // 결과 배열

        func recursive(startIndex : Int, Sum : Int){ //재귀함수. 시작index, 합계
            if Sum == target{ //합계가 목표와 같다면
                resultArray.append(middleArray) //결과 배열로 연산배열 append
                return //종료
            }
            if Sum > target{ // 합계가 목표보다 크다면,
                return //그대로 리턴
            }
            //핵심
            for i in startIndex..<candidates.count{ // 인덱스 별로 for loop
                middleArray.append(candidates[i]) //연산중인 배열에 startIndex의 원소 추가
                recursive(startIndex: i, Sum: Sum+candidates[i]) //재귀실행. i번째 인덱스와, i번째 인덱스의 원소 + 지금까지의 합을 더해서 재귀 함수로 리턴.
                middleArray.removeLast() // 백트래킹을 위해 맨 뒤 원소 삭제.
            }
        }
        
        recursive(startIndex: 0, Sum: 0) // 최초 재귀함수 호출. 초기화를 위해 0번째 인덱스와 합계 0부터 시작
        print(resultArray) // 디버깅을 위한 출력문
        return resultArray // 리턴은 결과 배열
    }
}
