// time: O(n), space: O(1)
// 투포인터로 양 끝에서 하나씩 줄여가며 가장 작은값 찾아 반환하기.
class Solution {
    func findMin(_ nums: [Int]) -> Int {
        guard nums.count != 1 else { return nums.first! }
        
        var answer = Int.max
        var left = 0
        var right = nums.count
        
        while right - left > 0 {
            let temp = min(nums[left], nums[right - 1])
            answer = min(answer, temp)
            left += 1
            right -= 1
        }

        return answer
    }
}
// time: O(log n), space: O(1)
// 중간 값과 오른쪽 값중 가장 작은쪽을 기준으로 잘라가며 탐색함 (이진 탐색)
class Solution {
    func findMin(_ nums: [Int]) -> Int {
        guard nums.count != 1 else { return nums.first! }
        
        var left = 0
        var right = nums.count - 1
        
        while left < right {
            let mid = (left + right) / 2
            if nums[mid] < nums[right] { right = mid }
            else { left = mid + 1 }
        }
        return nums[right]
    }
}

