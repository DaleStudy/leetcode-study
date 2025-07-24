class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var dictionary: [Int: Int] = [:]
        for num in nums {
            dictionary[num, default: 0] += 1
        }
        
        return dictionary.sorted(by: { $0.value > $1.value }).prefix(k).map(\.key)
    }
}
 
