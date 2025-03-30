class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var dict = [Int: Int]()
        for num in nums {
            dict[num, default: 0] += 1
        }
        return [Int](dict.sorted{$0.value > $1.value}.map{$0.key}[..<k])
    }
}
