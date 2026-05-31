class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var occurences = [Int: Bool]()

        for num in nums {
            if let occurs = occurences[num] {
                return occurs
            } else {
                occurences[num] = true
            }
        } 

        return false
    }
}
