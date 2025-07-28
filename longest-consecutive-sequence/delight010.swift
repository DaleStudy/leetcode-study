class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        if nums.isEmpty { return 0 }
        // .isEmpty 메서드를 사용하여 배열의 개수가 0일 시 바로 0을 리턴합니다.
        // 시간복잡도 O(1)
        var maxCount = 0
        var count = 1
        var prefixNumber = nums.sorted().first ?? 0
        for num in nums.sorted(by: <) {
            // nums 배열을 오름차순 정리 후 반복문을 루프합니다.
            // .sorted 시간복잡도 O(n log n)
            // for문 시간복잡도 O(n)
            if prefixNumber == num {
                continue
            } else if prefixNumber + 1 == num {
                count += 1
                prefixNumber = num
            } else {
                maxCount = max(maxCount, count)
                count = 1
                prefixNumber = num
            }
        }
        return max(maxCount, count)
    }
}
