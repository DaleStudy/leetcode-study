class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var dictionary: [Int: Int] = [:]
        for (index, num) in nums.enumerated() {
            // 배열 nums의 개수만큼 반복합니다. 시간복잡도 O(n)
            if let value = dictionary[num], value != index {
                return true
                // 만일 동일한 숫자를 일찍 찾게 된다면
                // 시간복잡도는 O(n)보다 더 빨라질 수 있습니다.
            }
            dictionary[num] = index
        }
        return false
    }
}
 
