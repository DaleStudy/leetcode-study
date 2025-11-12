class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var occurences = [Int: Int]()

        for num in nums {
            if let occurence = occurences[num] {
                occurences[num] = occurence + 1
            } else {
                occurences[num] = 1
            }
        }

        let numbers = occurences.keys.sorted { occurences[$0] ?? 0 > occurences[$1] ?? 0 }

        return Array(numbers[0..<k])
    }
}
