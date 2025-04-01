class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        /*
         중복 제거 후 소팅 후 배열로 만드는것은 N + NlogN + N 으로 예상된다..
         그래서 정렬만 하고 로직에서 중복 숫자는 그냥 무시하게 만드는 방식으로 속도를 개선
         문제에서 O(N)으로 작성하자 라는 제약아닌 제약이 있었는데, O(N)은 도저히 떠오르지 않는다.
        */
        let nums = nums.sorted()//Array(Set(nums).sorted())
        var answer = 1
        var count = 1
        for index in 0..<nums.count-1 {
            if nums[index] - nums[index + 1] == -1 {
                count += 1
            }
            else if nums[index] == nums[index + 1] { continue }
            else {
                answer = max(answer, count)
                count = 1
            }
        }
        return max(answer, count)
    }
}
