//
//  241.swift
//  Algorithm
//
//  Created by 안세훈 on 4/8/25.
//

//3Sum
class Solution { //정렬 + two pointer
    func threeSum(_ nums: [Int]) -> [[Int]] {
        let nums = nums.sorted() //배열을 오름차순으로 정렬
        var result: [[Int]] = [] // 결과를 저장할 배열.

        for i in 0..<nums.count { // i를 0번째 배열부터 순회.
            if i > 0 && nums[i] == nums[i - 1] {
                continue
            }

            var left = i + 1 //left는 i+1번째 인덱스
            var right = nums.count - 1 //right는 배열의 끝번째 인덱스

            while left < right {
                let sum = nums[i] + nums[left] + nums[right]

                if sum == 0 {
                    result.append([nums[i], nums[left], nums[right]])

                    // 중복 제거
                    while left < right && nums[left] == nums[left + 1] {
                        left += 1
                    }
                    while left < right && nums[right] == nums[right - 1] {
                        right -= 1
                    }

                    left += 1
                    right -= 1
                } else if sum < 0 {
                    left += 1
                } else {
                    right -= 1
                }
            }
        }

        return result
    }
}
