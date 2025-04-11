class Solution {
    // time: O(n2) space: O(n)..?
    func threeSum(_ nums: [Int]) -> [[Int]] {
        let nums = nums.sorted() // hashmap 방식으로는 안될거 같아 정렬후 순차탐색 하기
        
        var answer = Set<[Int]>() // 중복 제거를 위해 Set으로 선언
        for i in nums.indices {
            var left = i + 1
            var right = nums.count - 1
            while left < right {
                let result = nums[left] + nums[right] + nums[i]
                if result == 0 {
                    answer.insert([nums[i], nums[left], nums[right]])
                    // 포인터 옮겨주고 더 검사하기
                    right -= 1
                    left += 1
                }
                else if result > 0 {
                    right -= 1
                }
                else {
                    left += 1
                }
            }
        }
        return Array(answer)
    }
}
