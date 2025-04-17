///정수 배열 nums가 주어졌을 때,세 수의 합이 0이 되는 모든 삼중 조합 [nums[i], nums[j], nums[k]]을 반환하세요.
///i, j, k 모두 다른 인덱스, 같은 조합의 결과는 하나로 취급

class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        let sorted = nums.sorted()
        var result = [[Int]]()

        for i in 0..<sorted.count {
            // 중복 값 스킵
            if i > 0 && sorted[i] == sorted[i - 1] {
                continue
            }

            //포인터 설정
            var left = i + 1
            var right = sorted.count - 1

            //두 포인터가 만나기 전까지만
            while left < right {
                let sum = sorted[i] + sorted[left] + sorted[right]

                if sum == 0 {
                    result.append([sorted[i], sorted[left], sorted[right]])

                    // 같은 left/right 값 스킵
                    while left < right && sorted[left] == sorted[left + 1] {
                        left += 1
                    }
                    while left < right && sorted[right] == sorted[right - 1] {
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
