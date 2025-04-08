class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var tables: [Int: Int] = [:]
        
        for num in nums {
            tables[num] = (tables[num] ?? 0) + 1
        }
        
        let values = tables.values.sorted().reversed().prefix(k) // k개의 frequent
        let result = tables.compactMap { (key: Int, value: Int) -> Int? in
            if values.contains(value) {
                return key
            }
            return nil
        }
        return result
    }
}
