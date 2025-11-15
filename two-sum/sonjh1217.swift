class Solution {
    // time O(n) / space O(n)
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var indicesByCounters = [Int: Int]()
        for (i, num) in nums.enumerated() { 
            if let index = indicesByCounters[num] {
                return [index, i]
            }

            indicesByCounters[target - num] = i
        }

        return []
    }
}
